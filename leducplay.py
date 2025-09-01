import numpy as np
import random

class Leduc:

    def __init__(self):
        self.deck = np.array([0, 0, 1, 1, 2, 2])  # J=0, Q=1, K=2
        self.card_names = {0: 'J', 1: 'Q', 2: 'K'}

    # hist: (private_card, hole_card, round1_history, round2_history)
    @staticmethod
    def get_legal_actions(hist, round_num):
        current_hist = hist[round_num + 2]  # always action history
        if current_hist == '' or current_hist == 'x':
            return ['b', 'x']
        elif current_hist.count('r') < 2 and ('b' in current_hist or 'r' in current_hist):
            return ['c', 'f', 'r']
        else:
            return ['c', 'f']  # terminal states won't use these

    @staticmethod
    def round_over(hist, round_num):
        current_hist = hist[round_num + 2]
        return current_hist.endswith(('c', 'f')) or current_hist == 'xx'

    @staticmethod
    def is_terminal(hist, round_num):
        current_hist = hist[round_num + 2]
        # round 1- game ends only if someone folds
        if round_num == 0:
            return current_hist.endswith('f')
        # round 2- game ends on fold or showdown
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

    def play(self):
        np.random.shuffle(self.deck)
        p1_card = self.deck[0]
        p2_card = self.deck[1]
        hole_card = self.deck[2]
        print(f"P1: {self.card_names[p1_card]}, P2: {self.card_names[p2_card]}, Hole: {self.card_names[hole_card]}")

        hist = (p1_card, hole_card, '', '')
        round_num = 0

        while True:
            #check if game over to break game loop
            total_hist = hist[2] + hist[3]
            if total_hist.endswith('f') or (round_num == 2):
                break

            current_hist = hist[round_num + 2]
            current_player = 1 if len(current_hist) % 2 == 0 else 2

            legal_actions = self.get_legal_actions(hist, round_num)
            action = random.choice(legal_actions)
            print(f"Player {current_player} takes action: {action}")

            if round_num == 0:
                hist = (hist[0], hist[1], hist[2] + action, hist[3])
            else:
                hist = (hist[0], hist[1], hist[2], hist[3] + action)

            print(f"Current history: {hist[2]} | {hist[3]}")

            #next round if current round is over
            if self.round_over(hist, round_num):
                round_num += 1

        print(f"Final history: {hist[2]} | {hist[3]}")
        print(f"Player 1 payoff: {self.get_payoff(hist, p2_card)}")
        
pp = Leduc()
pp.play()