import math
from customFunctions import isFloat
def findMisSide(a, b, c):
    # Checks if more than 1 input is none and returns none as you needthe length 2 sides to find the third
    if (a==None and b==None) or (a==None and c==None) or (b==None and c==None) or (a==None and b==None and c==None):
        return None
    
    # Finds the missing side length of a RIGHT triangle
    if a==None:
        return math.sqrt((c**2)-(b**2))
    if b==None:
        return math.sqrt((c**2)-(a**2))
    if c==None:
        return math.sqrt((a**2)+(b**2))  
def distFormula(p1, p2):
    # Gets the distance on the coordinate plane of 2 points
    if (type(p1) == list) and (type(p2) == list):
        return math.sqrt(((p2[0]-p1[0])**2)+((p2[1]-p1[1])**2))
    else:
        return None
def inputNum(prompt):
    num = input(str(prompt))
    if num == "":
        return None
    if isFloat(num):
        return int(float(num))
    else:
        return None