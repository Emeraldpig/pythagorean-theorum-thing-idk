import math
from os import system
from mathFunctions import *
from customFunctions import *
true = True


while true:
    system('cls')
    while true:
        func = input("Find the missing side of a triangle or calculate distance formula? (miss/dist)").lower()
        if func == "miss" or func == "dist":
            break

    if func == "miss":
        system('cls')
        print("Input the length of EXACTLY 2 sides of the right triangle. Input nothing for the side which is unknown")
        while true:    
            a = inputNum("input length of side a: ")
            b = inputNum("input length of side b: ") 
            c = inputNum("input length of side c: ")
            varList = [a, b, c]
            if listContains(varList, None, 1):
                break
            else:
                system('cls')
                print("Only input side for exactly 2 sides and only input numbers")        
        print(findMisSide(a, b, c))
    
    elif func == "dist":
        print("Input the coordinates of the points")
        while true:
            x = inputNum("x of point 1: ")
            y = inputNum("y of point 1: ")
            x2 = inputNum("x of point 2: ")
            y2 = inputNum("y of point 2: ")
            if (isFloat(x)) and (isFloat(y)) and (isFloat(x2)) and (isFloat(y2)):
                break
            else:
                system('cls')
                print("make sure you input only NUMBERS")
        print(distFormula([x, y], [x2, y2]))  
    else:
        print("good job. you ruined it. you didnt input miss nor did you input dist. i could make it ask you again but why? why spend the time to fix something that you did that you could have very easily done properly. you purposely did this")  
    if input("continue?(y/n)") == "n":
        system('cls')
        break