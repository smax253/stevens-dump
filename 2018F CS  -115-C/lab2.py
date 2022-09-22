#I pledge my honor that I have abided by the Stevens Honor Code -Max Shi

def dot(L,K):
    '''Returns the dot product of the two lists, given that they are numbers and of the same length'''
    if L==[] or K==[]: return 0
    else: return L[0]*K[0]+dot(L[1:],K[1:])

def explode(S):
    '''Returns a list of individual characters in the given string'''
    if S == "": return []
    else: return [S[0]]+explode(S[1:])

def ind(e,L):
    '''Returns the index of the list L where element e is located. If e is not present, the length of the list will be returned.'''
    if L==[] or L=='' or L[0]==e: return 0
    else: return 1+ind(e,L[1:])

def removeAll(e,L):
    '''Returns a list with all elements e from the list L removed.'''
    if L==[]: return []
    elif L[0] == e: return []+removeAll(e,L[1:])
    else: return [L[0]]+removeAll(e,L[1:])

def myFilter(func, L):
    '''Returns a list which included all elements L for which func returned True'''
    if L==[]: return []
    elif func(L[0]): return [L[0]]+myFilter(func, L[1:])
    else: return [] + myFilter(func, L[1:])

def deepReverse(L):
    '''Returns a list where every element, including non-top-level elements, have been reversed'''
    if L==[]: return []
    elif isinstance(L[0], list):
        return deepReverse(L[1:])+[deepReverse(L[0])]
    else:
        return deepReverse(L[1:])+[L[0]]
