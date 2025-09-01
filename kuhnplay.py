import numpy as np
import random


class Kuhn:

    def __init__(self):
        self.deck=np.array([0,1,2]) # J=0, Q=1, K=2
        self.card_names=['J','Q','K']
    

    @staticmethod
    def get_legal_actions(hist:str):
        if hist == '':
            return ['b','x']
        elif hist in ['b','xb']:
            return ['c','f']
        else:
            return ['x','b']
        
    @staticmethod
    def is_terminal(hist: str):
        return hist in ['bc','bf','xx','xbc','xbf']
        
    def get_payoff(self,p1_card,p2_card,hist):
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
        




        
        

pp=Kuhn()
pp.play()

