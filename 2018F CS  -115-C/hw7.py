"""
    Hw7.py
    10/19/2018
    Max Shi
    I pledge my honor that I have abided by the Stevens Honor System
"""

def numToBaseB(N,B):
    '''Returns the represenation of number N in base 10 to base B'''
    if(N==0): return ""
    else: 
        rem = N%B
        return numToBaseB((N-rem)/B,B)+ str(int(rem))

def baseBToNum(S,B):
    """Returns the representation of a number as a string S in base B back to base 10"""
    if(S==''): return 0
    else: return int(S[-1])+B*baseBToNum(S[:-1],B)

def baseToBase(B1,B2,SinB1):
    """Returns the representation in base B2 of a string SinB1 in base B1"""
    return numToBaseB(baseBToNum(SinB1,B1),B2)

def add(S,T):
    """Adds two binary numbers together"""
    return numToBaseB(baseBToNum(S,2)+baseBToNum(T,2),2)

FullAdder = \
    { ('0','0','0') : ('0','0'), 
    ('0','0','1') : ('1','0'),
    ('0','1','0') : ('1','0'), 
    ('0','1','1') : ('0','1'),
    ('1','0','0') : ('1','0'), 
    ('1','0','1') : ('0','1'), 
    ('1','1','0') : ('0','1'), 
    ('1','1','1') : ('1','1') }
def addB(S,T):
    """Adds two binary numbers together with the binary method"""
    def add_helper(x,y,carry,acc):
        if(x=="" and y=="" and carry == "0"): return ""
        if x=="": x="0"
        if y=="": y="0"
        sum,carout = FullAdder[(x[-1],y[-1],carry)]
        if sum == "1": return add_helper(x[:-1],y[:-1],carout, 0)+sum+acc*'0'
        else: return add_helper(x[:-1],y[:-1],carout,acc+1)
    return add_helper(S,T,"0",0)
