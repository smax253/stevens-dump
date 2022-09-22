"""
    Max Shi
    11/7/2018
    Lab 10
    I pledge my honor that I have abided by the Stevens Honor System
"""
import sys, random

def createOneRow(width): 
    """ returns one row of zeros of width "width"...   
         You might use this in your createBoard(width, height) function """ 
    row = [] 
    for col in range(width): 
        row += [0] 
    return row 

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A+=[createOneRow(width)]
    return A

def printBoard(A):
    """ this function prints the 2d list-of-lists 
        A without spaces (using sys.stdout.write) 
    """ 
    for row in A: 
        for col in row: 
            sys.stdout.write( str(col) ) 
        sys.stdout.write( '\n' ) 

def diagonalize(width,height): 
    """ creates an empty board and then modifies it 
        so that it has a diagonal strip of "on" cells. 
    """ 
    A = createBoard( width, height ) 
    for row in range(height): 
        for col in range(width): 
            if row == col: 
                A[row][col] = 1 
            else: 
                A[row][col] = 0      
    return A 

def innerCells(w, h):
    """Creates a board of width w and height h with 0 on the walls and 1's on the inside"""
    board = createBoard(w,h)
    for row in range(1, h-1):
        for col in range(1, w-1):
            board[row][col] = 1
    return board

def randomCells(w,h):
    """Creates a board with width w and height h with randomized cells with the walls as 0"""
    board = createBoard(w,h)
    for row in range(1, h-1):
        for col in range(1,w-1):
            board[row][col] = random.choice([0,1])
    return board

def copy(A):
    """Returns a deep copy of the board A"""
    board = []
    for col in A:
        newcol = []
        for element in col:
            newcol += [element]
        board += [newcol]
    return board

def innerReverse(A):
    """Returns a new board that is a copy of A with all elements not on the edge reversed"""
    board = copy(A)
    for row in range(1, len(A)-1):
        for col in range(1, len(A[row])-1):
            board[row][col] = int(not board[row][col])
    return board

def countNeighbors(row,col,A):
    """Counts the number of neighbors in board A next to the cell in specified row and column"""
    values = [-1,1]
    neighbors = 0
    for x in values:
        if(A[row+x][col]): neighbors+=1
        if(A[row][col+x]): neighbors+=1
        if(A[row+x][col+x]): neighbors+=1
        if(A[row-x][col+x]): neighbors+=1
    return neighbors

def next_life_generation(A):
    """Generate the next generation within Conway's Game of Life Rules"""
    nextlife = createBoard(len(A[0]), len(A))
    for row in range(1,len(A)-1):
        for col in range(1,len(A[row])-1):
            if(countNeighbors(row, col, A)==3): nextlife[row][col] = 1
            elif(countNeighbors(row, col, A)==2 and A[row][col] == 1): nextlife[row][col] = 1
    return nextlife

