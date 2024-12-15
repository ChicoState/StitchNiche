"""
Utils holds a lot of useful functionalities

stitch_calculator is responsible for all mathematics done with stitches
"""
import random
import re
import traceback
import os
from uu import encode

import numpy

from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle

# for testing purposes
# can be commented out
def simple(input):
    return input

class StitchCalculator():
    def __init__(self):
        """
        Initializes pattern constraint information
        Parameter s_multiple: a pattern constraint (stitch_multiple)
        Precondition: s_multiple is a integer >= 1
        Parameter s_remainder: a pattern constraint (stitch_remainder)
        Precondition: s_remainder is an integer >= 0
        Parameter r_multiple: a pattern constraint (row_multiple)
        Precondition: r_multiple is a integer >= 1
        Parameter r_remainder: a pattern constraint (row_remainder)
        Precondition: r_remainder is an integer >= 0
        (self, stitch_multiple, stitch_remainder, row_multiple, row_remainder)
        
        """
        self.pattern = StitchPattern()
        pass

# arguments: string userIn, string mode
#            mode should be either "int" or "float" depending on which should be checked
# return: boolean, True means string is valid
    def setpattern(self, stitch_multiple, stitch_remainder, row_multiple, row_remainder) :
        self.pattern.setpattern(stitch_multiple, stitch_remainder, row_multiple, row_remainder)

    def isValid(self, userIn, mode, msg):
        isValid = True

        if (mode == "int"):
            if (not userIn.isdigit()):
                isValid = False
                msg.append("Number must be a positive integer!")

        elif (mode == "float"):
            try:
                float(userIn)
            except ValueError:
                msg.append("Number must be a valid float!")
                isValid = False

            if (re.search("-", userIn) != None):
                msg.append("Number must be positive!")
                isValid = False


        else:
            msg.append("Mode must be int or float")
            isValid = False

        return isValid

    def rectangle_calculator(self, width, length, gauge_l, gauge_w):
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

        """
        stitches = self.one_dim_calculator(width, gauge_w, True)
        rows = self.one_dim_calculator(length, gauge_l, False)
        return (stitches, rows)

    def one_dim_calculator(self, x, gauge, widthwise):
        """
        Finds the number of rows/stitches that will be closest in size to x while fitting pattern constraints:
        being equal to  n*multiple + remainder for some natural number, n

        Parameter x: 
        Precondition: x is a float > 0
        Parameter gauge: the number of stitches/rows per inch
        Precondition: gauge is a float > 0
        Parameter: widthwise is true if finding the number of stitches, not number of rows 
        """
        if (widthwise):
            multiple = self.pattern.smul
            remainder = self.pattern.srem
        else :
            multiple = self.pattern.rmul
            remainder = self.pattern.rrem

        estimate = int(x * gauge)
        if (x*gauge - estimate > 0.5) :
            estimate = estimate + 1

        difference = (estimate -  remainder)% multiple

        option1 = int(estimate - difference + multiple)
        option2 = int(estimate - difference)

        if difference > abs(multiple - difference):
            return option1
        else:
            return option2
            
    def change_width_calculator(self, starting_width, ending_width, length, gauge_l, gauge_w) :
        caston = self.one_dim_calculator(starting_width, gauge_w, True)
        castoff =  self.one_dim_calculator(ending_width, gauge_w, True)
        rownum = self.one_dim_calculator(length, gauge_l, False)

        numchanges = int(abs(castoff - caston) // self.pattern.smul)

        changingrows = {"row number": "increase/decrease by"}

        if(numchanges != 0):
            changingrows = self.distribute_change(rownum, changingrows, numchanges)
            
        return (caston, castoff, rownum, changingrows)


    def distribute_change(self, rownum, changingrows, numchanges) :
       """
       Evenly distributes increases and decreases through out the rows of a pattern
       """
       size = rownum
       n = size // numchanges
       m = 0
       if (numchanges > rownum):
           m = numchanges // rownum
           for i in range(1, rownum + 1):
               changingrows[i] = int(self.pattern.smul * m)
           numchanges = numchanges % rownum
           n = rownum // numchanges

       for i in range(1, rownum + 1, n):
           changingrows[i] = int(self.pattern.smul * (1 + m))
       return changingrows

class Styles:
    def __init__(self, label_color, header_color, size_hint, height, background_color, padding, spacing):
        self.label_color = label_color
        self.header_color = header_color
        self.size_hint = size_hint
        self.height = height
        self.background_color = background_color
        self.padding = padding
        self.spacing = spacing

class GenerateWidgets:
    def __init__(self):
        pass

    def generate_number_form(self, input_fields, styles, layout, submit_handler):
        scroll_view = ScrollView(size_hint=(1, None), height=Window.height * 1)
        form_layout = GridLayout(cols=3, padding=styles.padding, spacing=[styles.spacing, 10], size_hint_y=None)
        form_layout.bind(minimum_height=form_layout.setter('height'))

        text_inputs = {}
        tooltips = []

        def calculate_tooltip_width():
            return Window.width * 0.25

        for header, fields in input_fields.items():
            header_label = Label(text=header, color=styles.header_color, size_hint=(1, None), height=styles.height)
            form_layout.add_widget(header_label)
            form_layout.add_widget(Label())  # Empty for alignment
            form_layout.add_widget(Label())  # Empty for alignment

            for field_name, (label_text, default_value, tooltip_text) in fields.items():
                form_layout.add_widget(Label(text=label_text, color=styles.label_color, size_hint=(1, None), height=styles.height))

                text_input = TextInput(size_hint=(1, None), height=styles.height,
                                       background_color=styles.background_color, text=str(default_value))
                text_inputs[field_name] = text_input
                form_layout.add_widget(text_input)

                tooltip_label = Label(
                    text=tooltip_text,
                    color=styles.label_color,
                    size_hint=(None, None),
                    halign='left',
                    valign='middle',
                    text_size=(calculate_tooltip_width(), None),
                    width=calculate_tooltip_width(),
                    height=styles.height
                )
                tooltip_label.opacity = 0
                form_layout.add_widget(tooltip_label)

                tooltips.append(tooltip_label)

                text_input.bind(focus=lambda instance, value, tooltip=tooltip_label: setattr(tooltip, 'opacity', 1 if value else 0))

        def update_tooltips(*args):
            for tooltip in tooltips:
                new_width = calculate_tooltip_width()
                tooltip.width = new_width
                tooltip.text_size = (new_width, None)

        Window.bind(on_resize=update_tooltips)

        scroll_view.add_widget(form_layout)
        layout.add_widget(scroll_view)

        # Adjust result label position here:
       # Adjust result label position here:
         

        result = Label(text="Result", color=styles.header_color, size_hint=(None, None))
        result.width = Window.width * 0.8  # Ensure the width is within the screen width (adjust as needed)
        result.height = styles.height  # Set the height to match your desired height
        result.pos_hint = {"center_y": 0.5, "right": 0.9}  # Position as needed
        layout.add_widget(result)

        submit_button = Button(text="Submit", size_hint=(0.5, 0.5), height=styles.height * 0.2,
                            background_color=styles.background_color)
        submit_button.pos_hint = {"left": 0}  # Align the button to the left
        submit_button.bind(on_press=submit_handler)
        layout.add_widget(submit_button)

        return layout, text_inputs, result


    # stitches - columns
    # all vars must be natural numbers
    # smul, srem - s % smul = srem
    # rmul, rrem - r % rmul = rem
    # array: size = (smul*x + srem) * (rmul*y + rrem)

class StitchPattern:
    def __init__(self, stitch_multiple = 1, stitch_remainder = 0, row_multiple = 1, row_remainder = 0):
        self.smul = stitch_multiple
        self.srem = stitch_remainder
        self.rmul = row_multiple
        self.rrem = row_remainder

        self.id = str(random.randint(10000, 99999))
        self.pattern_matrix = None

    def setpattern(self, stitch_multiple = 1, stitch_remainder = 0, row_multiple = 1, row_remainder = 0):
        self.smul = stitch_multiple
        self.srem = stitch_remainder
        self.rmul = row_multiple
        self.rrem = row_remainder

    def full_save(self, matrix):
        try:
            print(matrix)
            print(len(matrix))
            print(matrix[0])
            encoded_pattern = self.encode(matrix, rows=len(matrix), columns=len(matrix[0]))
            self.save(self.id, encoded_pattern)
            return True
        except Exception as e:
            print("In StitchPattern:full_save: ", e)
            return False


    # input : 2d list   output: 2d list
    def encode(self, matrix, rows=10, columns=10):
        encoded_pattern = f"{self.smul},{self.srem},{self.rmul},{self.rrem}\n"
        for row in matrix[1:]:
            encoded_pattern += (",".join(map(str, row))) + '\n'
        print(encoded_pattern)
        return encoded_pattern # Return as single cohesive string

    def decode(self, input_string):
        # Split the string into lines
        lines = input_string.strip().split('\n')
        if not lines:
            raise ValueError("Input string is empty")

        # Extract the first line and parse the 4 ints
        first_line = lines[0].strip()
        first_line_ints = [int(x.strip()) for x in first_line.split(',')]
        if len(first_line_ints) != 4:
            raise ValueError("First line must contain exactly 4 integers")
        self.smul, self.srem, self.rmul, self.rrem = first_line_ints

        # Now parse the rest of the lines as the pattern matrix
        pattern_matrix = []
        for line in lines[1:]:
            line = line.strip()
            row = [int(x.strip()) for x in line.split(',')]
            pattern_matrix.append(row)
        self.pattern_matrix = pattern_matrix
        # probably want it to return True if it passes or something.

    # public, takes in 2d array pattern and passes to encoder to be saved as string in file
    def save(self, id, pattern):
        try:
            directory = "saved_patterns"       # make sure saved_patters dir exists
            if not os.path.exists(directory):
                os.makedirs(directory)

            with open("saved_patterns/"+id+str(random.randint(0, 5))+".txt", "w") as file:
                file.write(self.encode(pattern))
        except Exception as e:
            print("In StitchPattern:save: ", e)
            traceback.print_exc()

    # public, takes in id and returns 2d array from file
    def load(self, id):
        try:
            with open("saved_patterns" + id + ".txt", "r") as file:
                return self.decode(file.read())
        except Exception as e:
            print("In StitchPattern:load: ", e)
            traceback.print_exc()

class PatternVisualizer(BoxLayout):
    def __init__(self, matrix, color_value_map, **kwargs):
        super(PatternVisualizer, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Add the legend layout at the top
        legend_layout = BoxLayout(orientation='horizontal', size_hint_y=0.2, padding=(10, 10))
        for value, (text, color) in color_value_map.items():
            legend_layout.add_widget(LegendItem(text=text, color=color))
        self.add_widget(legend_layout)

        # Add the interactive grid of buttons
        self.pattern_matrix = PatternMatrix(matrix, color_value_map)
        self.add_widget(self.pattern_matrix)

    def get_matrix(self):
        return self.pattern_matrix.get_matrix()


class PatternMatrix(GridLayout):
    def __init__(self, matrix, color_value_map, **kwargs):
        super(PatternMatrix, self).__init__(**kwargs)
        self.cols = len(matrix[0])
        self.spacing = 5
        self.padding = 10

        # Store the color map and matrix
        self.color_value_map = color_value_map
        self.array = matrix

        # Dictionary to keep track of buttons and their positions
        self.buttons = {}

        for row in range(len(self.array)):
            for col in range(len(self.array[0])):
                value = self.array[row][col]
                color = self.value_to_color(value)
                btn = Button(background_normal="", background_color=color)
                btn.bind(on_press=self.change_color)
                # Store the button with its position
                self.buttons[btn] = (row, col)
                self.add_widget(btn)

    def value_to_color(self, value):
        return self.color_value_map.get(value, [1, 1, 1, 1])[1]  # Retrieve color from map

    def change_color(self, instance):
        row, col = self.buttons[instance]
        current_value = self.array[row][col]
        values = list(self.color_value_map.keys())
        next_value = values[(values.index(current_value) + 1) % len(values)]
        self.array[row][col] = next_value
        instance.background_color = self.value_to_color(next_value)

    def get_matrix(self):
        return self.array


class LegendItem(BoxLayout):
    def __init__(self, text, color, **kwargs):
        super(LegendItem, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = 0.7

        with self.canvas.before:
            Color(*color)  # Set the color from the color map
            self.rect = Rectangle(size=self.size, pos=self.pos)

        # Update the rectangle size and position when the widget changes
        self.bind(size=self.update_rect, pos=self.update_rect)
        self.add_widget(Label(text=text, size_hint_y=0.3))

    def update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos
