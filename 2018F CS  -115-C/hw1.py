from cs115 import reduce
#I pledge my honor that I have abided by the Stevens Honor System -Max Shi
def mult(x,y):
    '''Returns the product of x and y'''
    return x*y
def add(x,y):
    '''Returns the sum of x and y'''
    return x+y
def factorial(N):
    '''Returns the factorial of N'''
    return reduce(mult, range(1,N+1))
def mean(L):
    '''Returns the mean of the list L, which must be all numbers'''
    return reduce(add,L)*1.0/len(L)
def prime(N):
    '''Returns whether or not N is a prime number, True if prime, False if composite'''
    def div(x): return N%x!=0
    return N-reduce(add, map(div,range(1,N+1)))==2

