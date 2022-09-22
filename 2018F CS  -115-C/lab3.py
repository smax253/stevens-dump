"""
    Max Shi
    9/20/18
    I pledge my honor that I have abided by the Stevens Honor System
"""

def change(amt, coins):
    '''Returns the minimum number of coins necessary to pay the given value, returns infinity if impossible'''
    if amt == 0: return 0
    elif coins == []: return float("inf")
    elif coins[0]>amt: return change(amt,coins[1:])
    else:
        return min(1+change(amt-coins[0], coins),change(amt, coins[1:]))
