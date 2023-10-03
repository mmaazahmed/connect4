from random import randrange
from game import Connect4
class MinmaxAgent:
    ai_name=''
    def  __init__(self,name):
        self.ai_name=name

    def get_name(self):
        return self.ai_name
    def generate_world(self,Game,move):
        World=Connect4(Connect4.get_board(Game))
        self.get_utility(World,2)
        pass
    def get_utility(self,World,last_move):
        board=World.get_board()
        # if World.is_winning_move(last_move):
        #     return 10000000

        pass
    def get_move(self,Game):
        move=randrange(1,8)

        while not Connect4.is_valid_move(Game,move):
            move=randrange(1,8)
        self.generate_world(Game,move)

        return move-1