'''
Created on 10/10/18
@author:   Max Shi
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    return n%2==1

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0: return ''
    elif isOdd(n): return numToBinary((n-1)/2)+"1"
    else: return numToBinary(n/2) + "0"

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '': return 0
    else: return int(s[-1])+2*binaryToNum(s[:-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if(s==''): return ''
    elif(s[-1]=='1'): return increment(s[:-1])+'0'
    else: return s[:-1]+'1'

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if(n>0):  
        print(s)
        s=increment(s)
        count(s,n-1)
    else: print(s)
def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if(n==0): return ""
    else: 
        rem = n%3
        return numToTernary((n-rem)/3)+ str(int(rem))

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if(s==''): return 0
    else: return int(s[-1])+3*ternaryToNum(s[:-1])
