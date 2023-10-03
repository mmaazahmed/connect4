from random import randrange
from game import Connect4
from player import Player
from minmax_agent import MinmaxAgent
Connect4=Connect4()
def get_players():
    players=[]
    fighter=input("Choose your Fighter: 1:Human, 2:AI\n ")
    fighter_name=input("Enter figher name\n")
    opponent=input("Choose your Opponent: 1:Human, 2:AI\n")
    opponent_name=input("Enter opponent name\n")

    if int(fighter)==1:
        Player1=Player(fighter_name)
        players.append(Player1)
    else:
        Player1=MinmaxAgent(fighter_name)
        players.append(Player1)
    
    if int(opponent)==1:
        Player2=Player(opponent_name)
        players.append(Player2)
    else:
        Player2=MinmaxAgent(opponent_name)
        players.append(Player2)
    return players

def play(Game,isPlayerTurn,players):
    winner=''
    game_state=True
    round=1
    # player1=Player("player1")
    # Bob=MinmaxAgent('Bob')
    while game_state:
        if isPlayerTurn:
            player_move=players[0].get_move(Game)
            Connect4.drop_piece(player_move,'x')
            if Connect4.is_winning_move(player_move,'x'):
                game_state=False
                winner=players[0].get_name()
        else:
            ai_move=players[1].get_move(Game)
            Connect4.drop_piece(ai_move,'o')
            Connect4.display_board(round)
            round+=1
            if Connect4.is_winning_move(ai_move,'o'):
                game_state=False
                winner=players[1].get_name()

        isPlayerTurn= not (isPlayerTurn)
    Connect4.display_board(round)
    print("game won by",winner)



# def drop_piece(board,column,piece):
#     board[column]+=piece

# board=game.createBoard()
players=get_players()
board=Connect4.get_board()
play(Connect4,True,players)
