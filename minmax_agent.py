from random import randrange
from game import Connect4
class MinmaxAgent:
    ai_name=''
    def  __init__(self,name):
        self.ai_name=name
    def get_name(self):
        return self.ai_name
    def get_move(self,Game):
        move=randrange(1,8)
        while not Connect4.isValidMove(Game,move):
            move=randrange(1,8)
        return move-1