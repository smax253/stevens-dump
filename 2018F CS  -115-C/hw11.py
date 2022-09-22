"""
    Hw 11 - Nim
    Max Shi
    11/21/18
    I pledge my honor that I have abided by the Stevens Honor System
"""
# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)
from cs115 import reduce,map
from random import *
def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:

            print("You won!")

            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:

            print("The computer won!")

            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles
    userinput = -1
    while(userinput<1):
        try:
            userinput = int(input("How many piles in this game of Nim? "))
        except ValueError:
            userinput = -1
    num_piles = userinput
    userinput = -1
    for pile in range(num_piles):
        while(userinput < 1):
            try:
                userinput = int(input("What is the size of pile "+str(pile+1)+"? "))
            except ValueError:
                userinput = -1
        piles += [userinput]
        userinput = -1
    pass

        
def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles
    for pile in range(num_piles):
        print("Pile "+str(pile+1)+": "+str(piles[pile]))
    pass # TODO 


def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p-1] = piles[p-1] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles
    userinput = 0
    while (userinput<1 or userinput>num_piles):
        try:
            userinput = int(input("Which pile would you like to remove from? "))
        except ValueError:
            userinput = 0
    return userinput


def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles
    userinput = 0
    while (userinput < 1 or userinput > piles[pnum-1]):
        try:
            userinput = int(input("How many would you like to remove from pile "+str(pnum)+"? "))
        except ValueError:
            userinput = 0
    return userinput


def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles 
    return reduce(lambda x,y: x^y, piles)

def rand_play():
    global piles
    global num_piles
    n = randint(0,num_piles-1)
    p = randint(1,piles[n])
    return (n,p)

def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles 
    nimsum = game_nim_sum()
    pilesums = map(lambda x: x^nimsum, piles)
    #print(nimsum)
    #print(pilesums)
    index = 0
    while(index<num_piles and piles[index]<=pilesums[index]):
        index+=1
    if index == num_piles:
        return rand_play()
    else:
        n = piles[index] - pilesums[index]
        return (index,n)



def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles
    pile, amt = opt_play()
    piles[pile] -= amt
    print("The computer removed "+str(amt)+" from pile "+str(pile+1)+".")
    pass

    


#   start playing automatically
if __name__ == "__main__" : play_nim()
