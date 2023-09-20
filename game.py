def createBoard():
    board= ['','','','','','','']
    return board

def display_board(board,round):
    print("round No",round)
    print(1,2,3,4,5,6,7)

    # print(0,1,2,3,4,5,6)
    for j in reversed(range(6)):
        col=''
        for i in range(7):
            if j<len(board[i]):
                col+=(board[i][j])
            else:
                col+="-"
            col+='|'
        print(col)


def is_winning_vertical(board,move,piece):
    return (board[move][-4:].count(piece)==4)



def is_winning_horizontal(board,move,piece):
    COL=7
    row=len(board[move])-1 
    count=0
    for col in range(move,COL):
        # print(col,"col")
        if row>len(board[col])-1 or board[col][row]!=piece:
            break
        count+=1

    for col in reversed(range(move)):
        if row>len(board[col])-1 or board[col][row]!=piece:
            break
        count+=1

    return (count>=4)
def is_winning_positive_diagonal(board,move,piece):
    count=0
    row=len(board[move])
    col=move+1

    for i in range(1,row+1):
        if row-i<0 or col-i<0 or (len(board[col-i])<=row-i) or board[col-i][row-i]!=piece:
            break
        count+=1
    
    for i in range(7-row):
        if row+i>=6 or col+i>=7 or (len(board[col+i])<=row+i)or board[col+i][row+i]!=piece :
            break
    
        count+=1
    return (count>=4)

def is_winning_negative_diagonal(board,move,piece):
    count=0
    row=len(board[move])-1
    col=move
    for i in range(1,6-row):
        if row+i>=6 or col-i<0 or (len(board[col-i])<=row+i or board[col-i][row+i]!=piece ) :
            break     
        count+=1
    for i in range(row+1):
        if (row-i<0 or col+i>6) or (len(board[col+i])<=row-i) or board[col+i][row-i]!=piece:
            break
        count+=1

    return (count>=4)


        


def isWinningMove(board,move,piece):
    print("im here")
    game_info=(board,move,piece)
    return (is_winning_vertical(board,move,piece) or is_winning_negative_diagonal(board,move,piece)  or 
            is_winning_positive_diagonal(board,move,piece) or is_winning_horizontal(board,move,piece)  )

def isValidMove(board,move):
    if (move<1 or move>7):
        print("invalid input please input value between 1 and 7")
        return False
    if (len(board[move-1])>=6):
        print("Col is full, please select different colum")
        return False
    return True