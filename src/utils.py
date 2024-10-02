"""
Utils holds a lot of useful functionalities

stitch_calculator is responsible for all mathematics done with stitches
"""
import re

class StitchCalculator():
    def __init__(self):
        pass

# arguments: string userIn, string mode
#            mode should be either "int" or "float" depending on which should be checked
# return: boolean, True means string is valid

    def isValid(self, userIn, mode):
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

    def rectangle_calculator(self, gauge_w, width, s_multiple, s_remainder, gauge_l, length, r_multiple, r_remainder ):
        stitches = self.one_dim_calculator(gauge_w, width, s_multiple, s_remainder)
        rows = self.one_dim_calculator(gauge_l, length, r_multiple, r_remainder)
        return (stitches, rows)

    def one_dim_calculator(self, gauge, x, multiple , remainder):
        estimate = int(x / gauge)
        difference = estimate % multiple
        if difference == remainder:
            return estimate
        elif difference + 1 == remainder:
            return estimate + 1
        else:
            option1 = difference - remainder
            option2 = difference + remainder
            return min((option1, option2))

class GenerateWidgets():
    def __init__(self):
        pass

    # Create a form
    # labels is a dictionary like {"input1" : 0.0}, first being the label, second being the type
    def generate_number_form(self, labels, styles):
        pass