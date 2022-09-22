from cs115 import reduce, map,range
import math

def inverse(N):
    """Returns the inverse of N"""
    return 1.0/N

def add(x,y):
    """Returns sum of x and y"""
    return x+y
def e(N):
    """Returns an approximation of e using N amount of terms in a taylor expansion"""
    return 1+reduce(add,map(inverse,map(math.factorial,range(1,N+1))))
def error(N):
    """Returns the difference between the approximation of e with the taylor expansion of N terms and the actual value"""
    return abs(math.e-e(N))

#I pledge my honor that I have abided by the Stevens Honor System -Max Shi
