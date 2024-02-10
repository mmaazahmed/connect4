from random import randrange
from game import Connect4
from player import Player
from minmax_agent import MinmaxAgent
Connect4=Connect4()
def get_players():
    players = []
    for i in range(2):
        player_type = input(f"Choose your Player {i+1}: 1: Human, 2: AI\n ")
        player_name = input(f"Enter player {i+1} name\n")

        player = Player(player_name) if player_type == '1' else MinmaxAgent(player_name)
        players.append(player)

    return players

def play(Game,isPlayerTurn,players):
    winner=''
    game_state=True
    current_round=1
    while  True:
        current_player=players[0] if isPlayerTurn else players[1]
        piece='x'if isPlayerTurn else 'o'
        column=current_player.get_move(Game)
        Connect4.drop_piece(player_move, piece )

        if Connect4.is_winning_move(player_move,piece):
            winner=current_player.get_name()
            break
        
        if not isPlayerTurn:
            Connect4.display_board(current_round)
    
        isPlayerTurn= not (isPlayerTurn)
        current_round+=1
    Connect4.display_board(round)
    print("game won by",winner)



# def drop_piece(board,column,piece):
#     board[column]+=piece

# board=game.createBoard()
players=get_players()
board=Connect4.get_board()
play(Connect4,True,players)
