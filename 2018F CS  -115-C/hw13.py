"""
    Max Shi
    HW 13
    12/3/18
    I pledge my honor that I have abided by the Stevens Honor System
"""

class Board:
    def __init__(self, width = 7, height = 6):
        """Initialize the game board with default values for a connect four board or specified values."""
        self.__gameBoard = []
        self.__width = width
        self.__height = height
        for col in range(width):
            self.__gameBoard += [[]]
            #print(self.__gameBoard)
            for row in range(height):
                self.__gameBoard[col] += " "

    def __str__(self):
        """Converts the board into a string representation to be printed"""
        s = ""
        for row in range(self.__height):
            s+="|"
            for col in range(self.__width):
                s+=self.__gameBoard[col][row]
                s+="|"
            s+="\n"
        s+="-"*(self.__width*2+1)+"\n"
        for col in range(self.__width):
            s+=" "+str(col)
        return s+"\n"

    def allowsMove(self, col):
        """Returns whether there is a possible move in a column of the game board"""
        return self.__gameBoard[col][0] == " "
    
    def addMove(self, col, ox):
        """Adds a move to the specified column on the board with symbol ox"""
        if self.allowsMove(col):
            topindex = 0
            while(topindex<self.__height and self.__gameBoard[col][topindex]==" "):
                topindex+=1
            self.__gameBoard[col][topindex-1] = ox
            return True
        else: return False
    
    def setBoard( self, moveString ):
        """ takes in a string of columns and places
        alternating checkers in those columns,
        starting with 'X'
        For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the
        bottom row, or b.setBoard('000000') to
        see them alternate in the left column.
        moveString must be a string of integers
        """
        nextCh = 'X'   # start by playing 'X'
        for colString in moveString:
            col = int(colString)
            if 0 <= col <= self.__width:
                self.addMove(col, nextCh)
            if nextCh == 'X': nextCh = 'O'
            else: nextCh = 'X'
            
    def delMove(self, col):
        """Deletes the last move in the column in the board"""
        for column in self.__gameBoard:
            for entry in column:
                if entry != " ":
                    entry = " "
                    break

    def winsFor(self, ox):
        """Checks if player ox has 4 connected pieces"""
        maxRow = self.__height-3
        maxCol = self.__width-3
        for col in range(self.__width):
            for row in range(self.__height):
                if col<maxCol:
                    #check horiz
                    if(self.__gameBoard[col][row] == ox):
                        curCol = col+1
                        counter = 1
                        while counter<4 and self.__gameBoard[curCol][row] == ox:
                            curCol += 1
                            counter += 1
                        if counter == 4:
                            return True
                if row<maxRow:
                    #check vert
                    if(self.__gameBoard[col][row] == ox):
                        curRow = row + 1
                        counter = 1
                        while counter<4 and self.__gameBoard[col][curRow] == ox:
                            curRow += 1
                            counter += 1
                        if counter == 4:
                            return True
                if row<maxRow and col<maxCol:
                    #check SE diag
                    if(self.__gameBoard[col][row] == ox):
                        curRow = row + 1
                        curCol = col + 1
                        counter = 1
                        while counter<4 and self.__gameBoard[curCol][curRow] == ox:
                            curRow+=1
                            curCol+=1
                            counter+=1
                        if counter == 4:
                            return True
                if row>2 and col<maxCol:
                    #check NE diag
                    if self.__gameBoard[col][row] == ox:
                        curRow = row-1
                        curCol = col+1
                        counter = 1
                        while counter<4 and self.__gameBoard[curCol][curRow] == ox:
                            curRow -= 1
                            curCol += 1
                            counter += 1
                        if counter == 4:
                             return True
        return False
    
    def hostGame(self):
        """Hosts a game on a standard connect four board between O and X"""
        gameDone = False
        turn = "X"
        turncount = 0
        while not gameDone and turncount<42:
            xInput = -1
            while (xInput<0 or xInput>self.__width) or not self.allowsMove(xInput):
                try:
                    xInput = int(input("Input "+turn+"'s move: "))
                except ValueError:
                    xInput = -1
            self.addMove(xInput, turn)
            print(self)
            if self.winsFor(turn):
                print(turn+" wins!")
                gameDone = True
            elif turn=="X": turn = "O"
            else: turn = "X"
            turncount+=1
        if not gameDone:
            print("It's a tie!")


