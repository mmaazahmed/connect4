import game

class Player:
    player_name=''
    def __init__(self,name):
        self.player_name=name
    def get_name(self):
        return self.player_name
    def get_move(self,board):
        print("input value between 1 and 7")
        move=int(input('enter move:'))
        while not game.isValidMove(board,move):
            move=int(input('enter move:'))

        return move-1
    

