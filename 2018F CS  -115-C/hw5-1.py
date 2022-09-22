'''
Created on 10/5/18
@author:   Max Shi
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Hw 5
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

def sv_tree(trunk_length, levels):
    if levels != 0:
        turtle.forward(trunk_length)
        turtle.left(45)
        sv_tree(trunk_length/2, levels-1)
        turtle.left(90)
        sv_tree(trunk_length/2, levels-1)
        turtle.left(45)
        turtle.forward(trunk_length)
        

lucasmemo = {0:2,
             1:1}
def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    if(n in lucasmemo): return lucasmemo[n]
    else: 
        lucasmemo[n] = fast_lucas(n-1)+fast_lucas(n-2)
        return lucasmemo[n]

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amt, coins, memo):
        if(amt in memo): return memo[amt]
        if amt == 0: return [0,[]]
        elif coins == (): return [float("inf"),[]]
        elif coins[0]>amt: return fast_change_helper(amt,coins[1:],memo)
        else:
            useList = fast_change_helper(amt-coins[0],coins,memo)
            use = [(1+useList[0]),([coins[0]]+useList[1])]
            loseList = fast_change_helper(amt,coins[1:],memo)
            lose = [loseList[0],loseList[1]]
            sol = use if use[0]<lose[0] else lose
            memo[amt] = sol
            return sol

    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})[0]

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)
