
import numpy as np
import random
import itertools
import matplotlib.pyplot as plt


class Leduc:

    def __init__(self):
        self.deck = np.array([0, 0, 1, 1, 2, 2])  # J=0, Q=1, K=2
        self.card_names = {0: 'J', 1: 'Q', 2: 'K'}
        self.nodes = {}  # dictionary to store nodes for CFR

    # hist: (private_card, hole_card, round1_history, round2_history)
    @staticmethod
    def get_legal_actions(hist, round_num):
        # make sure hist is correct format
        if isinstance(hist, tuple):
            hist = list(hist)
        idx = round_num + 2
        current_hist = hist[idx] if idx < len(hist) and hist[idx] is not None else ''
        # normalize
        if current_hist == '' or current_hist == 'x':
            return ['b', 'x']
        # bet or raise
        if current_hist.count('r') < 1 and ('b' in current_hist or 'r' in current_hist):
            return ['c', 'f', 'r']
        return ['c', 'f']  #terminal cases won't use anyway

    @staticmethod
    def round_over(hist, round_num):
        if isinstance(hist, tuple):
            hist = list(hist)
        idx = round_num + 2
        current_hist = hist[idx] if idx < len(hist) and hist[idx] is not None else ''
        return current_hist.endswith(('c', 'f')) or current_hist == 'xx'

    @staticmethod
    def is_terminal(hist, round_num):
        if isinstance(hist, tuple):
            hist = list(hist)
        idx = round_num + 2
        current_hist = hist[idx] if idx < len(hist) and hist[idx] is not None else ''
        # round 0: game ends only if someone folds in the first round
        if round_num == 0:
            return current_hist.endswith('f')
        # round 1 (second round): ends on fold or showdown
        return current_hist.endswith(('c', 'f')) or current_hist == 'xx'

    @staticmethod
    def pair_winner(p1_card, p2_card, hole):
        if p1_card == p2_card:
            return 0  # tie
        elif hole == p1_card:
            return 1
        elif hole == p2_card:
            return 2
        else:
            return 1 if p1_card > p2_card else 2

    def get_payoff(self, hist, p2_card):
        p1_contrib = 0
        p2_contrib = 0
        folded = (hist[2] + hist[3]).endswith('f')

        for round_num in range(2):
            round_hist= hist[round_num+2]
            current_player=1
            bet_size = 2 if round_num == 0 else 4
            for action in round_hist:
                if action in ('b', 'c'):
                    if current_player == 1:
                        p1_contrib += bet_size
                    else:
                        p2_contrib += bet_size
                elif action == 'r':
                    if current_player == 1:
                        p1_contrib += 2*bet_size
                    else:
                        p2_contrib += 2*bet_size
                current_player = 2 if current_player == 1 else 1

        if not folded:
            assert p1_contrib == p2_contrib, f"unmatched contributions in {hist}"

        p1_input = 1 + p1_contrib
        pot = 2 + p1_contrib + p2_contrib

        if folded:
            #save history of round where fold happened
            fold_hist = hist[2] if hist[2].endswith('f') else hist[3]
            #check parity of fold history to determine who folded
            if len(fold_hist) % 2 == 0:
                return pot - p1_input  
            else:
                return -p1_input
        else: #showdown branch
            winner = self.pair_winner(hist[0], p2_card, hist[1])
            if winner == 0:
                return 0  # tie
            elif winner == 1:
                return pot - p1_input
            else:
                return -p1_input






    def cfr(self, hist, p2_card, round_no, p1_reach, p2_reach, hole_card):
        # hist right format
        if isinstance(hist, tuple):
            hist = list(hist)
        while len(hist) < 4:
            hist.append('')
        current_round = round_no
        new_hist = hist.copy()
        # advance only if the round ended but not terminal
        if self.round_over(new_hist, current_round) and not self.is_terminal(new_hist, current_round):
            current_round += 1
            # reveal hole card on going to next round
            new_hist[1] = hole_card

        # If we've advanced past round 1 and round 2 is terminal, return payoff
        if current_round >= 2:
            # terminal check for round 1/2 combined
            if self.is_terminal(new_hist, 1):
                return self.get_payoff(new_hist, p2_card)
        #  node check at current round
        if self.is_terminal(new_hist, current_round):
            return self.get_payoff(new_hist, p2_card)
        # work out current player based on action count 
        round_hist = new_hist[current_round + 2]
        current_player = 1 if len(round_hist) % 2 == 0 else 2
        curr_prob = p1_reach if current_player == 1 else p2_reach
        opp_prob = p2_reach if current_player == 1 else p1_reach

        current_player_card = new_hist[0] if current_player == 1 else p2_card

        legal_actions = self.get_legal_actions(new_hist, current_round) # legal actions at this node
        hole_question = 'None' if new_hist[1] is None else self.card_names[new_hist[1]]
        key = f'{self.card_names[current_player_card]}|{hole_question}|r{current_round}|{new_hist[2]}|{new_hist[3]}' # create node key based on available info

        if key not in self.nodes:
            self.nodes[key] = Node(key, legal_actions)
        current_node = self.nodes[key]

        node_strategy = current_node.get_strategy()
        current_node.update_total_strategy(node_strategy, curr_prob)

        # CFR recursion over legal actions
        action_values = []
        for i, action in enumerate(legal_actions):
            action_chance = node_strategy[i]
            next_hist = new_hist.copy()

            next_hist[current_round + 2] = next_hist[current_round + 2] + action


            next_round = current_round# next round logic
            if self.round_over(next_hist, current_round) and not self.is_terminal(next_hist, current_round):
                next_round += 1
                if next_hist[1] in (None, ''):
                    next_hist[1] = hole_card

            # recursion w/ updated reach probs
            if current_player == 1:
                val = self.cfr(tuple(next_hist), p2_card, next_round, p1_reach * action_chance, p2_reach, hole_card)
            else:
                val = self.cfr(tuple(next_hist), p2_card, next_round, p1_reach, p2_reach * action_chance, hole_card)
            action_values.append(val)

        action_values = np.array(action_values)
        node_value_p1 = np.dot(action_values, node_strategy)
        #get regrets
        player_value = action_values if current_player == 1 else -action_values
        node_value_player = np.dot(player_value, node_strategy)
        regrets = player_value - node_value_player
        current_node.update_regrets(regrets, opp_prob)

        return node_value_p1

    def evaluate(self, hist, p2_card, round_no, hole_card):
            # hist right format
            if isinstance(hist, tuple):
                hist = list(hist)
            while len(hist) < 4:
                hist.append('')
            current_round = round_no
            new_hist = hist.copy()
            # advance only if the round ended but not terminal
            if self.round_over(new_hist, current_round) and not self.is_terminal(new_hist, current_round):
                current_round += 1
                # reveal hole card on going to next round
                new_hist[1] = hole_card
    
            #  node check at current round
            if self.is_terminal(new_hist, current_round):
                return self.get_payoff(new_hist, p2_card)
            # work out current player based on action count 
            round_hist = new_hist[current_round + 2]
            current_player = 1 if len(round_hist) % 2 == 0 else 2
    
            current_player_card = new_hist[0] if current_player == 1 else p2_card
    
            legal_actions = self.get_legal_actions(new_hist, current_round) # legal actions at this node
            hole_question = 'None' if new_hist[1] is None else self.card_names[new_hist[1]]
            key = f'{self.card_names[current_player_card]}|{hole_question}|r{current_round}|{new_hist[2]}|{new_hist[3]}' # create node key based on available info
    
            if key not in self.nodes:
                raise KeyError(f"unvisited infoset: {key}")
            strategy = self.nodes[key].get_avg_strategy_array()
    
            
    
            # CFR recursion over legal actions
            total=0.0
            for i, action in enumerate(legal_actions):
                action_chance = strategy[i]
                next_hist = new_hist.copy()
    
                next_hist[current_round + 2] = next_hist[current_round + 2] + action

    

                val = self.evaluate(tuple(next_hist), p2_card, current_round, hole_card)
                total += action_chance * val
    
            return total
    
    def initial_weights(self, my_card):
        #return a dictionary of {(opponent_card, hole_card):probability} given my_card
        #don't use continue as it throws away duplicates
        weights = {}
        for perm in itertools.permutations(self.deck, 3):
            if perm[0] == my_card:
                weights[(perm[1], perm[2])] = weights.get((perm[1], perm[2]), 0) + 1
        for key in weights:
            weights[key] /= 120
        return weights
    
    def br_value(self, my_card, board, hist, round_no, weights, br_player):
        hist = list(hist)
        while len(hist) < 4:
            hist.append('')

        # round transition: the board becomes public, so split the hidden state
        if (self.round_over(hist, round_no)
                and not self.is_terminal(hist, round_no)
                and board is None):
            total = 0.0
            for b in (0, 1, 2):
                sub = {k: w for k, w in weights.items() if k[1] == b}
                if not sub:
                    continue
                next_hist = hist.copy()
                next_hist[1] = b
                total += self.br_value(my_card, b, next_hist, round_no + 1, sub, br_player)
            return total

        # terminal: sum weight * payoff over every hidden state
        if self.is_terminal(hist, round_no):
            total = 0.0
            for (opp_card, _), w in weights.items():
                if br_player == 1:
                    total += w * self.get_payoff(hist, opp_card)
                else:
                    h = hist.copy()
                    h[0] = opp_card
                    total += w * -self.get_payoff(h, my_card)
            return total

        current_player = 1 if len(hist[round_no + 2]) % 2 == 0 else 2
        legal_actions = self.get_legal_actions(hist, round_no)

        if current_player == br_player:
            # my node: max over values already summed across every hidden state,
            # so it's one action per infoset rather than per deal
            values = []
            for action in legal_actions:
                next_hist = hist.copy()
                next_hist[round_no + 2] += action
                values.append(
                    self.br_value(my_card, board, next_hist, round_no, weights, br_player))
            return max(values)

        # opponent's node: scale each weight by their probability of the action
        # given the card in that key
        hole_q = 'None' if hist[1] is None else self.card_names[hist[1]]
        total = 0.0
        for i, action in enumerate(legal_actions):
            sub = {}
            for k, w in weights.items():
                key = f'{self.card_names[k[0]]}|{hole_q}|r{round_no}|{hist[2]}|{hist[3]}'
                sub[k] = w * self.nodes[key].get_avg_strategy_array()[i]
            next_hist = hist.copy()
            next_hist[round_no + 2] += action
            total += self.br_value(my_card, board, next_hist, round_no, sub, br_player)
        return total


    def exploitability(self):
        total = 0.0
        for br_player in (1, 2):
            for card in (0, 1, 2):
                w = self.initial_weights(card)
                total += self.br_value(card, None, [card, None, '', ''], 0, w, br_player)
        return total

    
    def train(self, iterations: int):
        for _ in range(iterations):
            for permutation in itertools.permutations(self.deck, 3):
                starting_hist = (permutation[0], None, '', '')
                self.cfr(starting_hist, permutation[1], 0, 1, 1, permutation[2])
        avg_strategies = {key: node.get_avg_strategy() for key, node in self.nodes.items()}
        return avg_strategies  # having run CFR and updated nodes, return the updated avg. strategy

    def get_game_value(self):
        total = 0.0
        for permutation in itertools.permutations(self.deck, 3):
            total += self.evaluate((permutation[0], None, '', ''), permutation[1], 0, permutation[2])
        return total / 120


class Node:

    def __init__(self, key, actions):
        self.key = key
        self.actions = actions
        self.actions_number = len(actions)
        self.cum_regrets = np.zeros(self.actions_number)
        self.current_strategy = np.array([1 / self.actions_number] * self.actions_number)
        self.total_strategy = np.zeros(self.actions_number)

    def get_strategy(self):
        floored_regrets = np.maximum(self.cum_regrets, 0)
        regret_total = floored_regrets.sum()
        if regret_total > 0:
            return floored_regrets / regret_total
        else:
            return np.array([1 / self.actions_number] * self.actions_number)

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
        return {self.actions[i]: round(float(avg_strategy[i]), 2) for i in range(self.actions_number)}

    def get_avg_strategy_array(self):
            total = self.total_strategy.sum()
            if total > 0:
                avg_strategy = self.total_strategy / total
            else:
                avg_strategy = np.array([1 / self.actions_number] * self.actions_number)
            return avg_strategy

'''
if __name__ == "__main__": # loop running cfr for training over x iterations and printing the resulting strategies and game value
    pp = Leduc()
    strategies = pp.train(3000)   
    for i, (key, strat) in enumerate(strategies.items()):
        print(f"Node {key}: {strat}")
    print(f"Game value for Player 1: {pp.get_game_value()}")
    print(f'Nodes visited: {len(pp.nodes)}')
'''

if __name__ == "__main__":
    pp = Leduc()
    checkpoints = [100, 200, 400, 800, 1600, 3200]

    xs, expls, values = [], [], []
    done = 0
    for target in checkpoints:
        pp.train(target - done)
        done = target
        expl = pp.exploitability() / 2      # drop the /2 for NashConv
        value = pp.get_game_value()
        xs.append(target)
        expls.append(expl)
        values.append(value)
        print(f'{target:>6}  value {value:+.5f}   exploitability {expl:.5f}')

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))

    ax1.loglog(xs, expls, marker='o', label='CFR')
    ax1.loglog(xs, [expls[-1] * (xs[-1] / x) ** 0.5 for x in xs],
               '--', alpha=0.5, label='1/√T')
    ax1.set_xlabel('iterations')
    ax1.set_ylabel('exploitability (chips/hand)')
    ax1.set_title('Exploitability')
    ax1.grid(True, which='both', alpha=0.3)
    ax1.legend()

    ax2.semilogx(xs, values, marker='o', color='tab:blue', label='self-play value')
    ax2.axhline(-0.085606424078, color='tab:red', ls='--', alpha=0.7, label='true value')
    ax2.set_xlabel('iterations')
    ax2.set_ylabel('game value for P1 (chips/hand)')
    ax2.set_title('Self-play value')
    ax2.grid(True, which='both', alpha=0.3)
    ax2.legend()

    fig.suptitle("Leduc Hold'em — vanilla CFR convergence")
    fig.tight_layout()
    fig.savefig('convergence.png', dpi=150, bbox_inches='tight')
    plt.show()