"""
Utils holds a lot of useful functionalities

stitch_calculator is responsible for all mathematics done with stitches
"""
import re

class stitch_calculator():
    def __init__():
        pass


# arguments: string userIn, string mode
#            mode should be either "int" or "float" depending on which should be checked
# return: boolean, True means string is valid

def isValid(userIn, mode):
    isValid = True
    
    if (mode == "int"):
        if (not userIn.isdigit()):
            isValid = False
            print("Number must be a positive integer!")

    elif (mode == "float"):
        try:
            float(userIn)
        except ValueError:
            print("Number must be a valid float!")
            isValid = False

        if (re.search("-", userIn) != None):
            print("Number must be positive!")
            isValid = False


    else:
        print("Mode must be int or float")
        isValid = False
        
    return isValid
