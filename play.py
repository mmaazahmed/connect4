from random import randrange
import game
from player import Player

def get_ai_move(board):
    move=randrange(1,8)
    while not game.isValidMove(board,move):
        move=randrange(1,8)
    return move-1

def play(board,isPlayerTurn):
    winner=''
    game_state=True
    round=1
    player1=Player("player1")
    while game_state:
        if isPlayerTurn:
            player_move=player1.get_move(board)
            drop_piece(board,player_move,'x')
            if game.isWinningMove(board,player_move,'x'):
                game_state=False
                winner=player1.get_name()
        else:
            ai_move=get_ai_move(board)
            drop_piece(board,ai_move,'o')
            game.display_board(board,round)
            round+=1
            if game.isWinningMove(board,ai_move,'o'):
                game_state=False
                winner='AI, getf'

        isPlayerTurn= not (isPlayerTurn)
    game.display_board(board,round)
    print("game won by",winner)



def drop_piece(board,column,piece):
    board[column]+=piece
    # return not isWinningMove(board,column,piece)

board=game.createBoard()
play(board,True)
# board= ['xxxxxx','o','o','','oo','o','o']
# is_winning_horizontal(board,4,'o')
# display_board(board)

# x()