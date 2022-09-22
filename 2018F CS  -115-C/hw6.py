'''
Created on 10/13/18
@author:   Max Shi
Pledge:    I pledge my honor that I have abided by the Stevens Honor System
CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5
# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1
# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def increment(s):
    '''Precondition: s is a string of n bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if(s==''): return ''
    elif(s[-1]=='1'): return increment(s[:-1])+'0'
    else: return s[:-1]+'1'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '': return 0
    else: return int(s[-1])+2*binaryToNum(s[:-1])

def compress(s):
    '''Returns a compressed version of string s with run length encoding with max length defined in file'''
    def compress_helper(encode, state, num):
        '''compresses the encode string with a state boolean using num as an accumulator'''
        if encode == '': return num
        elif(num == "1"*COMPRESSED_BLOCK_SIZE): return num + compress_helper(encode,not state, "0"*COMPRESSED_BLOCK_SIZE)
        elif int(encode[0]) == int(state):
            return compress_helper(encode[1:],state,increment(num))
        else:
            return num + compress_helper(encode,not state, "0"*COMPRESSED_BLOCK_SIZE)
    return compress_helper(s,False,"0"*COMPRESSED_BLOCK_SIZE)

def uncompress(s):
    '''Returns the uncompressed string compressed with the compress() function'''
    def uncompress_helper(decode, state):
        '''uncompresses the decode string using state boolean'''
        if decode == "": return ""
        else: return binaryToNum(decode[:COMPRESSED_BLOCK_SIZE])*str(int(state)) + uncompress_helper(decode[COMPRESSED_BLOCK_SIZE:],not state)
    return uncompress_helper(s,False)

def compression(s):
    '''Returns the ratio of the length between compress and the original string'''
    def comp_length(comp):
        '''Returns the length of comp'''
        if comp == "": return 0
        else: return 1 + comp_length(comp[1:])
    return comp_length(compress(s))/comp_length(s)
'''
    1. If every bit is different compared to the last one, starting with a 1, the compressed string would have length of 5*64+5 or 5*65.
    2. An entirely white square -- "0"*64 -- 0.390625
    An entirely black square -- "1"*64 -- 0.46875
    A checkerboard -- "01"*32 -- 5.0
    print(compression("0"*64))
    print(compression("1"*64))
    print(compression("01"*32))
    3. Laicompress is impossible because of the way to compress a string such as the one in comment 1.
    In order to compress that string, run-length encoding cannot be used, and binary values have to represent patterns.
    Run-length encoding cannot be used because each run would be length 1, the only way to make it the smallest size possible is making the 
    maximum run length 1, which makes the encoded value still the same length.
    Therefore, binary values must represent patterns. However, two bits have four possible patterns, which will need two bits to encode, three bits have eight possible patterns, which need three bits to encode, and so forth.
    Therefore, this algorithm is impossible.
'''
