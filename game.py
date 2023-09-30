class Connect4:
    board=['','','','','','','']

    def __init__(self):
        pass

    def get_board(self):
        return self.board

    def display_board(self,round):
        print("round No",round)
        print(1,2,3,4,5,6,7)
        # print(0,1,2,3,4,5,6)
        for j in reversed(range(6)):
            col=''
            for i in range(7):
                if j<len(self.board[i]):
                    col+=(self.board[i][j])
                else:
                    col+="-"
                col+='|'
            print(col)


    def is_winning_vertical(self,move,piece):
        return (self.board[move][-4:].count(piece)==4)

    def is_winning_horizontal(self,move,piece):
        COL=7
        row=len(self.board[move])-1 
        count=0

        for col in range(move,COL):
            # print(col,"col")
            if row>len(self.board[col])-1 or self.board[col][row]!=piece:
                break
            count+=1
        for col in reversed(range(move)):
            if row>len(self.board[col])-1 or self.board[col][row]!=piece:
                break
            count+=1

        return (count>=4)
    
    def is_winning_positive_diagonal(self,move,piece):
        count=0
        row=len(self.board[move])
        col=move+1

        for i in range(1,row+1):
            if row-i<0 or col-i<0 or (len(self.board[col-i])<=row-i) or self.board[col-i][row-i]!=piece:
                break
            count+=1
        
        for i in range(7-row):
            if row+i>=6 or col+i>=7 or (len(self.board[col+i])<=row+i)or self.board[col+i][row+i]!=piece :
                break
        
            count+=1
        return (count>=4)

    def is_winning_negative_diagonal(self,move,piece):
        count=0
        row=len(self.board[move])-1
        col=move
        for i in range(1,6-row):
            if row+i>=6 or col-i<0 or (len(self.board[col-i])<=row+i or self.board[col-i][row+i]!=piece ) :
                break     
            count+=1
        for i in range(row+1):
            if (row-i<0 or col+i>6) or (len(self.board[col+i])<=row-i) or self.board[col+i][row-i]!=piece:
                break
            count+=1

        return (count>=4)


            


    def isWinningMove(self,move,piece):
        return (self.is_winning_vertical(move,piece) or self.is_winning_negative_diagonal(move,piece)  or 
                self.is_winning_positive_diagonal(move,piece) or self.is_winning_horizontal(move,piece)  )

    def isValidMove(self,move):
        if (move<1 or move>7):
            print("invalid input please input value between 1 and 7")
            return False
        if (len(self.board[move-1])>=6):
            print("Col is full, please select different colum")
            return False
        return True


    def drop_piece(self,column,piece):
        self.board[column]+=piece
