from random import randrange

a=1
def x():
    print(game_state)

def createBoard():
    board= ['','','','','','','']
    return board

def display_board(board):
    print(1,2,3,4,5,6,7)
    for j in reversed(range(6)):
        col=''
        for i in range(7):
            if j<len(board[i]):
                col+=(board[i][j])
            else:
                col+="-"
            col+='|'
        print(col)

def play(board,isPlayerTurn):
    winner=''
    game_state=True
    while game_state:
        winner=drop_piece(board,isPlayerTurn)
        isPlayerTurn= not isPlayerTurn
        if isPlayerTurn:
            display_board(board)
    print("game won by",winner)

def isWinningMove(board,move,piece):
    print("im here")
    if ( board[move][-4:].count(piece)==4 ): 
        return True
    
    

def get_ai_move(board):
    move=randrange(1,8)
    while not isValidMove(board,move):
        move=randrange(1,8)
    return move-1

def isValidMove(board,move):
    if (move<1 or move>7):
        print("invalid input please input value between 1 and 7")
        return False
    if (len(board[move-1])>=6):
        print("Col is full, please select different colum")
        return False
    return True
    
def get_player_move(board):
    print("input value between 1 and 7")
    move=int(input('enter move:'))
    while not isValidMove(board,move):
        move=int(input('enter move:'))

    return move-1
    

def drop_piece(board,isPlayerTurn):
    winner=''
    global game_state

    if isPlayerTurn:
        move=get_player_move(board)
        board[move]+='x'
        if  isWinningMove(board,move,'x'):
            game_state=False
            winner="player"
    else:
        move=get_ai_move(board)
        board[move]+='o'
        if isWinningMove(board,move,'o'):
            # global game_state
            game_state= False
            winner="comp"
    return winner




board=createBoard()
play(board,True)
# x()