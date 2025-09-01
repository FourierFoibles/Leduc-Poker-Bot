import numpy as np
import random


class Kuhn:

    def __init__(self):
        self.deck=np.array([0,1,2]) # J=0, Q=1, K=2
        self.card_names=['J','Q','K']
        self.nodes={} #dictionary which will be used to store nodes as CFR recursively creates and stores them
    

    @staticmethod
    def get_legal_actions(hist: str):
        if hist == '':
            return ['b','x']#p1 first action
        elif hist == 'x':
          return ['b','x']#p2 after p1 check
        elif hist == 'b':
            return ['c','f']# p2 after p1 bet
        elif hist == 'xb':
            return ['c','f']# p1 after p2 bet following check
        else:
            return []#no legal actions      
        
    @staticmethod
    def is_terminal(hist: str):
        return hist in ['bc','bf','xx','xbc','xbf']#determine if the game has ended by checking if history matches a terminal state
        
    def get_payoff(self,p1_card,p2_card,hist): #hardcoded payoffs for Kuhn poker
        high_card='Player 1' if p1_card>p2_card else 'Player 2'

        if hist == 'bc':
            if high_card == 'Player 1':
                return 2
            else:
                return -2
        elif hist == 'bf':
            return 1
        elif hist == 'xx':
            if high_card == 'Player 1':
                return 1
            else:
                return -1
        elif hist == 'xbc':
            if high_card == 'Player 1':
                return 2
            else:
                return -2
        elif hist == 'xbf':
            return -1
        
    def train(self, iterations: int):
        for _ in range(iterations): # loop over all possible card deals 
            for i in range(3):
                for j in range(3):
                    if i == j:
                        continue #skip if both players have the same card
                    self.cfr(i, j, '', 1.0, 1.0) #run cfr with the current cards specified in the loop (by i and j), so on each iteration we run through each equally likely deal)
        avg_strategies = {key: node.get_avg_strategy() for key, node in self.nodes.items()}
        return avg_strategies # having run CFR and updated nodes, return the updated avg. strategy of form {'P1 card +hstory':{probs for each action}}
        
    def cfr(self,p1_card,p2_card,hist:str,p1_reach,p2_reach):
        current_player= 1 if len(hist) % 2 ==0 else 2
        if current_player == 1:
            curr_prob = p1_reach
            opp_prob = p2_reach
        else:
            curr_prob = p2_reach
            opp_prob = p1_reach

        current_player_card=p1_card if current_player==1 else p2_card

        if self.is_terminal(hist):
            return self.get_payoff(p1_card,p2_card,hist) #value of terminal node if the payoff for Player 1 (P2's value will be the negative of that)
        else: #otherwise we check the node we are at, look for all the legal actions and get the strategy profile
            key = self.card_names[current_player_card] + hist
            if key not in self.nodes:
                self.nodes[key] = Node(key, self.get_legal_actions(hist))
            current_node = self.nodes[key]
            node_strategy=current_node.get_strategy()
            current_node.update_total_strategy(node_strategy, curr_prob)#since we use the strategy in this iteration, we update the total strategy weighted by the reach prob
            legal_actions=self.get_legal_actions(hist)
            action_values=[]
            for i in range(len(legal_actions)):
                action=legal_actions[i]
                action_chance=node_strategy[i]
                next_action_history=hist+action

                #next we create an array which represents how much each action value is worth from the current node (mathematical expectation)

                if current_player ==1:
                    action_values.append(self.cfr(p1_card,p2_card,next_action_history,p1_reach*action_chance,p2_reach))
                else:
                    action_values.append(self.cfr(p1_card,p2_card,next_action_history,p1_reach,p2_reach*action_chance))
            action_values=np.array(action_values)

            node_value_p1 = np.dot(action_values, node_strategy)

            #regret are computed based on the value to the current player
            # for p1 use action_values, for p2 use -action_values
            if current_player == 1:
                player_value = action_values
            else:
                player_value = -action_values

            node_value_player = np.dot(player_value, node_strategy)# calculates mathematical expected value of node
            
            regrets = player_value - node_value_player # regret is how much an action is worth - the expected value of the node
            current_node.update_regrets(regrets, opp_prob)# update regrets weighted by opponent reach 
        return node_value_p1
    
    def get_game_value(self,iterations):
        game_value=0
        for _ in range(iterations): #same loop as in cfr (all card deals equally likely) 
            for i in range(3):
                for j in range(3):
                    if i == j:
                        continue 
                    game_value+=self.cfr(i, j, '', 1.0, 1.0)#add together the game value for p1 in each cfr runthrough
        return game_value/ (iterations*6) #divide by number of iterations and number of deals to get average game value for p1

class Node:

    def __init__(self, key, actions):
        self.key=key
        self.actions=actions
        self.actions_number=len(actions)
        self.cum_regrets=np.zeros(self.actions_number)
        self.current_strategy=np.array([1/self.actions_number]*self.actions_number) #initialise the strategy as equal chacne for all
        self.total_strategy=np.zeros(self.actions_number)


    def get_strategy(self):
        floored_regrets=np.maximum(self.cum_regrets,0) # to get a strategy only consider positive regrets (we add both positive and negative regret to cumulative , then temporarily 0 negative values when calculating a strategy)
        regret_total=floored_regrets.sum()
        if regret_total>0:
            return floored_regrets/regret_total
        else:
            return np.array([1/self.actions_number]*self.actions_number) #fallback to uniform strategy
    def update_total_strategy(self, nd_strat, curr_reach_prob):
        self.total_strategy += nd_strat * curr_reach_prob

    def update_regrets(self, inst_regrets, opp_reach_prob):
        self.cum_regrets += inst_regrets * opp_reach_prob

    def get_avg_strategy(self):
        total = self.total_strategy.sum()
        if total > 0:
            avg_strategy = self.total_strategy / total
        else:
            avg_strategy = np.array([1 / self.actions_number] * self.actions_number)
        return {self.actions[i]: round(float(avg_strategy[i]),2) for i in range(self.actions_number)}
    
game = Kuhn()
avg_strategies = game.train(10000)

# sort nodes: J,Q,K first (hist ''), then by card order and history order (x, b, xb)
order_map = {'J': 0, 'Q': 1, 'K': 2}
hist_order = {'': 0, 'x': 1, 'b': 2, 'xb': 3}

def sort_key(k):
    card = k[0]
    hist = k[1:]
    return (order_map.get(card), hist_order.get(hist))

for key in sorted(avg_strategies.keys(), key=sort_key):
    player_turn='Player 2 Turn:' if len(key) % 2==0 else 'Player 1 Turn:'
    print(f"{player_turn} Node {key}: {avg_strategies[key]}")
print(f"Game value for Player 1: {round(game.get_game_value(10000),3)}")
