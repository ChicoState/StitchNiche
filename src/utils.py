"""
Utils holds a lot of useful functionalities

stitch_calculator is responsible for all mathematics done with stitches
"""
import re

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

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

    def rectangle_calculator(self, width, length, gauge_l, gauge_w, s_multiple, s_remainder, r_multiple, r_remainder ):
        """
        Calculates the number stitches to cast on and rows to complete to make a rectangle of size width * length,
        while fitting the pattern constraints

        Parameter width: 
        Precondition: width is a float > 0
        Parameter length: 
        Precondition: length is a float > 0
        Parameter gauge_l: the number of rows per inch
        Precondition: gauge is a float > 0
        Parameter gauge_w: the number of stitches per inch
        Precondition: gauge is a float > 0
        Parameter s_multiple: a pattern constraint (stitch_multiple)
        Precondition: s_multiple is a integer >= 1
        Parameter s_remainder: a pattern constraint (stitch_remainder)
        Precondition: s_remainder is an integer >= 0
        Parameter r_multiple: a pattern constraint (row_multiple)
        Precondition: r_multiple is a integer >= 1
        Parameter r_remainder: a pattern constraint (row_remainder)
        Precondition: r_remainder is an integer >= 0
        :return: (number of stitches to cast on: integer, number of rows to complete: integer)
        """
        stitches = self.one_dim_calculator(width, gauge_w, s_multiple, s_remainder)
        rows = self.one_dim_calculator(length, gauge_l, r_multiple, r_remainder)
        return (stitches, rows)

    def one_dim_calculator(self, x, gauge, multiple , remainder):
        """
        Finds the number of rows/stitches that will be closest in size to x while fitting pattern constraints:
        being equal to  n*multiple + remainder for some natural number, n

        Parameter x: 
        Precondition: x is a float > 0
        Parameter gauge: the number of stitches/rows per inch
        Precondition: gauge is a float > 0
        Parameter multiple: a pattern constraint
        Precondition: multiple is a integer >= 1
        Parameter remainder: a pattern constraint
        Precondition: remainder is an integer >= 0
        :return: integer best fit for stitch/row number to be x wide/long 
        """
        estimate = int(x * gauge)
        difference = (estimate -  remainder)% multiple
        if difference == 0:
            return estimate
        elif difference  == 1:
            return estimate + 1
        else:
            option1 = estimate - difference + multiple
            option2 = estimate - difference
            if difference > abs(multiple - difference):
                return option1
            else:
                return option2

class Styles():
    def __init__(self, color, size_hint, height, background_color, padding, spacing):
        self.color = color
        self.size_hint = size_hint
        self.height = height
        self.background_color = background_color
        self.padding = padding
        self.spacing = spacing

class GenerateWidgets():
    def __init__(self):
        pass

    # Create a form
    # labels is a dictionary like {"input1" : 0.0}, first being the label, second being the type
    def generate_number_form(self, cols, labels, styles, layout, submit_handler):
        form_layout = GridLayout(cols=cols, padding=styles.padding, spacing=styles.spacing, size_hint=(1, 1))
        text_inputs = {}
        for name in labels:
            form_layout.add_widget(Label(text=name, color=styles.color))
            text_inputs[name] = TextInput(size_hint=styles.size_hint, height=styles.height, background_color=styles.background_color)
            form_layout.add_widget(text_inputs[name])
        layout.add_widget(form_layout)
        layout.add_widget(Label(text="Result", color=styles.color))
        submit_button = Button(text="Submit", size_hint=styles.size_hint, height=styles.height, background_color=styles.background_color)
        submit_button.bind(on_press=submit_handler)
        layout.add_widget(submit_button)
        return layout, text_inputs
