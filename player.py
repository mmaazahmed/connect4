from game import Connect4

class Player:
    player_name=''
    def __init__(self,name):
        self.player_name=name
    def get_name(self):
        return self.player_name
    def get_move(self,Game):
        print("input value between 1 and 7")
        move=int(input('enter move:'))
        while not Connect4.isValidMove(Game,move):
            move=int(input('enter move:'))

        return move-1
    

