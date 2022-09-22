"""
    Max Shi
    9/26/18
    I pledge my honor that I have abided by the Stevens Honor System
"""

def adjSum(L):

    '''Returns a list of the sums of the given elements in the list'''
    if L[0] == 1: L=L+[0]
    if L[1] == 0: return []
    else: return [L[0]+L[1]]+adjSum(L[1:])
def pascal_row(N):
    '''Returns the given row N of Pascal's Triangle'''
    if N == 0: return [1]
    else: return [1]+adjSum(pascal_row(N-1))+[1]
def pascal_triangle(N):
    '''Returns a list of Pascal's triangle's rows from row 0 up to row N'''
    if(N==0): return [[1]]
    else: return pascal_triangle(N-1)+[pascal_row(N)]
def test_pascal_row():
    '''Runs four test cases on pascal_row(N)'''
    assert(pascal_row(3) == [1,3,3,1])
    assert(pascal_row(10)== [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1])
    assert(pascal_row(0) == [1])
    assert(pascal_row(5) == [1, 5, 10, 10, 5, 1])
def test_pascal_triangle():
    '''Runs four test cases on pascal_triangle(N)'''
    assert(pascal_triangle(3) ==[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])
    assert(pascal_triangle(5) ==[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]])
    assert(pascal_triangle(0) ==[[1]])
    assert(pascal_triangle(1) ==[[1],[1,1]])
