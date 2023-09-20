from random import randrange
from connect4 import isValidmove

def get_ai_move(board):
    move=randrange(1,8)
    while not isValidMove(board,move):
        move=randrange(1,8)
    return move-1