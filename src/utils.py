"""
Utils holds a lot of useful functionalities

stitch_calculator is responsible for all mathematics done with stitches
"""
import re

import numpy

from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

class StitchCalculator():
    def __init__(self, stitch_multiple, stitch_remainder, row_multiple, row_remainder):
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
        
        """
        pattern = StitchPattern(stitch_multiple, stitch_remainder, row_multiple, row_remainder)
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

        :return: (number of stitches to cast on: integer, number of rows to complete: integer)
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
    def change_width_calculator(self, starting_width, ending_width, length, gauge_l, gauge_w) :
        caston = self.one_dim_calculator(starting_width, gauge_w, True)
        castoff =  self.one_dim_calculator(ending_width, gauge_w, True)
        rownum = self.one_dim_calculator(length, gauge_l, False)

        numchanges = abs(castoff - caston) // self.pattern.smul

        rows = numpy.zeros(rownum)

        rows = self.distribute_change(rows, numchanges)
        rows *= self.pattern.smul

        return (caston, castoff, rows)


    def distribute_change(self, rows, numchanges) :
       """
       Evenly distributes increases and decreases through out the rows of a pattern
       """
       size = rows.size()
       if (numchanges >= size) :
            m = numchanges // size
            rows += m
            numchanges %= size
            
        n = size // numchanges
        for i in range(0, rows.size(), n)
            rows[i] +=1
        return rows


        


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
        scroll_view = ScrollView(size_hint=(1, 6))
        form_layout = GridLayout(cols=3, padding=styles.padding, spacing=[styles.spacing, 10], size_hint_y=None)
        form_layout.bind(minimum_height=form_layout.setter('height'))  # Adjust height dynamically

        text_inputs = {}
        tooltips = []

        def calculate_tooltip_width():
            return Window.width * 0.25

        for header, fields in input_fields.items():
            # Add header label spanning all columns
            header_label = Label(text=header, color=styles.header_color, size_hint=(1, None), height=styles.height)
            form_layout.add_widget(header_label)
            form_layout.add_widget(Label())  # Empty for alignment
            form_layout.add_widget(Label())  # Empty for alignment

            for field_name, (label_text, default_value, tooltip_text) in fields.items():
                form_layout.add_widget(Label(text=label_text, color=styles.label_color, size_hint=(0.2, None), height=styles.height))

                text_input = TextInput(size_hint=(0.4, None), height=styles.height,
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

        result = Label(text="Result", color=styles.header_color)
        layout.add_widget(result)

        submit_button = Button(text="Submit", size_hint=styles.size_hint, height=styles.height,
                               background_color=styles.background_color)
        submit_button.bind(on_press=submit_handler)
        layout.add_widget(submit_button)

        return layout, text_inputs, result

class StitchPattern:
    def __init__(self, stitch_multiple, stitch_remainder, row_multiple, row_remainder):
        self.smul = stitch_multiple
        self.srem = stitch_remainder
        self.rmul = row_multiple
        self.rrem = row_remainder

    def encode(self):
        pass

    def save(self):
        pass

    def load(self):
        pass

class PatternVisualizer:
    def __init__(self):
        pass;