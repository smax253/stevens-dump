'''
Created on 9/18/18
@author:   Max Shi
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.
def remove(e,L):
    '''Returns a list with the first element e from the list L removed.'''
    if L==[]: return []
    elif L[0] == e: return L[1:]
    else: return [L[0]]+remove(e,L[1:])
    

def myTwoFilter(func, L, S):
    '''Returns a list which includes all elements S for given L for which func returned True'''
    if S==[]: return []
    elif func(L,S[0]): return [S[0]]+myTwoFilter(func,L, S[1:])
    else: return [] + myTwoFilter(func,L, S[1:])

def letterScore(letter, scoreList):
    '''Returns the score associated with the given letter. The letter must be in the score list.'''
    if(scoreList[0][0] == letter): return scoreList[0][1]
    else: return letterScore(letter, scoreList[1:])

def wordScore(S, scoreList):
    '''Returns the total score of the word in the scorelist. Each letter in the word must be in the scorelist.'''
    if(S==''): return 0
    else: return letterScore(S[0],scoreList)+wordScore(S[1:],scoreList)
    
def wordPossible(Rack, word):
    '''Returns whether or not the word is able to be made with the given rack'''
    if word == "": return True
    elif word[0] in Rack: return wordPossible(remove(word[0],Rack),word[1:])
    else: return False
    
def scoreList(Rack):
    '''Returns all the possible words with their scores from the given rack'''
    return map(lambda x:[x,wordScore(x,scrabbleScores)],myTwoFilter(wordPossible,Rack, Dictionary))

def bestWord(Rack):
    '''Returns the best word and its score that can be made from the given rack'''
    return reduce(lambda x,y:x if x[1]>y[1] else y,[['',0]]+scoreList(Rack))
    

    
