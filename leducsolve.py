import numpy as np
import random
import itertools


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
        # bet or raise and not more than 2 raises yet
        if current_hist.count('r') < 2 and ('b' in current_hist or 'r' in current_hist):
            return ['c', 'f', 'r']
        return ['c', 'f']  # terminal cases won't use anyway

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
        pot = 2  # starting pot
        p1_input = 1

        for round_num in range(2):
            bet_size = 2 if round_num == 0 else 4
            current_player = 0
            for action in hist[round_num + 2]:
                if action in ['b', 'r', 'c']:
                    pot += bet_size
                    if current_player == 0:
                        p1_input += bet_size
                current_player = 1 - current_player

        total_hist = hist[2] + hist[3]

        # someone folded
        if total_hist.endswith('f'):
            if len(total_hist) % 2 == 1:  # p1 folded
                return -p1_input
            else:  # p2 folded
                return pot - p1_input

        # showdown/pair comparison
        winner = self.pair_winner(hist[0], p2_card, hist[1])
        if winner == 1:
            return pot - p1_input
        elif winner == 2:
            return -p1_input
        else:
            return 0

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

    def train(self, iterations: int):
        for _ in range(iterations):
            for permutation in itertools.permutations(self.deck, 3):
                starting_hist = (permutation[0], None, '', '')
                self.cfr(starting_hist, permutation[1], 0, 1, 1, permutation[2])
        avg_strategies = {key: node.get_avg_strategy() for key, node in self.nodes.items()}
        return avg_strategies  # having run CFR and updated nodes, return the updated avg. strategy

    def get_game_value(self, iterations):
        game_value = 0
        for _ in range(iterations):
            for permutation in itertools.permutations(self.deck, 3):
                starting_hist = (permutation[0], None, '', '')
                game_value += self.cfr(starting_hist, permutation[1], 0, 1, 1, permutation[2])
        return game_value / (iterations * 120)  # average over iterations and deals (6P3 = 120)


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


if __name__ == "__main__": # loop running cfr for training over x iterations and printing the resulting strategies and game value
    pp = Leduc()
    strategies = pp.train(500)   
    for i, (key, strat) in enumerate(strategies.items()):
        print(f"Node {key}: {strat}")
    print(f"Game value for Player 1: {pp.get_game_value(500)}")

