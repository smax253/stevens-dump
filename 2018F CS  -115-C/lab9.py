"""
    Lab 9
    Max Shi
    10/29/18
    I pledge my honor that I have abided by the Stevens Honor System
"""
from cs5png import *   # You may already have this line... 

def mult(c, n):
    """Returns c times an integer n using only addition"""
    result = 0
    for x in range(n):
        result += c
    return result

def update(c,n):
    """ update starts with z=0 and runs z = z**2 + c 
    for a total of n times. It returns the final z.  
    """ 
    result = 0
    for x in range(n):
        result = result**2 + c
    return result

def inMSet(c,n):
    """ inMSet takes in  
            c for the update step of z = z**2+c 
            n, the maximum number of times to run that step 
        Then, it should return  
            False as soon as abs(z) gets larger than 2 
            True if abs(z) never gets larger than 2 (for n iterations) 
    """ 
    result = 0
    for x in range(n):
        result = result**2 + c
        if abs(result)>2: return False
    return True

def scale(pix, pixMax, floatMin, floatMax):
    """Returns a float based on the row or column compared to the maximum row or column and the bounds between the two min and max floats"""
    percent = 1.0*pix/pixMax
    total = floatMax-floatMin
    return total*percent+floatMin

def mandlebrot(width, height):
    """Prints mandlebrot set with given width and height"""
    n=25
    image = PNGImage(width, height)
    for col in range(width):
        for row in range(height):
            c = scale(col, width, -2.0, 1.0) + scale(row, height, -1.0,1.0)*1j
            if inMSet(c, n):
                image.plotPoint(col, row)
    image.saveFile()
