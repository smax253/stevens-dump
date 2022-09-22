"""
    Max Shi
    9/26/18
    I pledge my honor that I have abided by the Stevens Honor System
"""

def knapsack(cap, items):
    '''Returns the maximum value and the list of items that can be created out of the subset of the items given with the given capacity'''
    if items == []: return [0,[]]
    elif items[0][0]>cap: return knapsack(cap, items[1:])
    else:
        use = knapsack(cap-items[0][0],items[1:])
        useList = [items[0][1]+use[0],[items[0]]+use[1]]
        lose = knapsack(cap,items[1:])
        return useList if useList[0]>lose[0] else lose
