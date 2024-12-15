
import os
import sys
from email.quoprimime import header_decode
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivy.uix.scrollview import ScrollView
from utils import Styles
# Import the StitchCalculator class
from utils import StitchCalculator
from utils import GenerateWidgets
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch') # remove red dots on ctrl-click

class ChangeWidthPage(Screen):
    def __init__(self, **kwargs):
        super(ChangeWidthPage, self).__init__(**kwargs)
        from homePage import NavDrawer
        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)
        nav_drawer = NavDrawer(self)

        # nav_bar handles nav_drawer
        nav_bar = MDTopAppBar(title="Stitch Calculator - Change Width",md_bg_color=(0.5, 0, 0.5, 1))
        # opens nav_drawer on click
        nav_bar.left_action_items = [["menu", lambda x: nav_drawer.set_state("toggle")]]
        layout.add_widget(nav_bar)

        self.sc = StitchCalculator()   
        
        # form
        style = Styles(
            label_color=(0.5, 0, 0.5, 1),
            header_color = (0.8, 0, 0.1),
            size_hint=(1, 1),
            height=35,
            background_color=(1, 1, 1, 1),
            padding=5,
            spacing=10
        )
        input_fields = {
            "Project Measurements:": {                                                                              # header
                "start_width_input": (                                                                                # variable associated with input
                    "Starting Width Input",                                                                              # label text for input
                    "35.0",                                                                                      # default value
                    "How wide your finished piece should be at first row. Can be entered as a decimal or whole number." # tooltip
                ),
                "end_width_input": (  # variable associated with input
                    "Ending Width Input",  # label text for input
                    "45.0",  # default value
                    "How wide your finished piece should be at final row. Can be entered as a decimal or whole number."
                # tooltip
                ),
                "length_input": (
                    "Length Input",
                    "10.0",
                    "How long you want your finished piece to be. Can be entered as a decimal or whole number."
                ),
                "gauge_width_input": (
                    "Gauge Width Input",
                    "5.0",
                    "The ratio of stitches to an inch for your specific pattern worked by you. Calculated by dividing the count of stitches within a section of a row by the width of that section. Can be entered as a decimal or whole number."
                ),
                "gauge_length_input": (
                    "Gauge Length Input",
                    "6.0",
                    "The ratio of rows to an inch for your specific pattern worked by you. Calculated by dividing the count of rows within a section of length by the length of the section. Can be entered as a decimal or whole number."
                )
            },
            "Pattern:": {
                "Stitch Multiple": (
                    "Stitch Multiple",
                    "5",
                    "Based on the constraints your pattern has for casting on, if your pattern calls for working a multiple of x stitches plus y, your stitch_multiple is x. If it doesn’t have any requirements, enter 1. This value is always a whole number."
                ),
                "Stitch Remainder": (
                    "Stitch Remainder",
                    "0",
                    "Based on the constraints your pattern has for casting on, if your pattern calls for working a multiple of x stitches plus y, your stitch_remainder is y. If it doesn’t have any requirements or just calls for a multiple x, enter 0. This value is always a whole number."
                ),
                "Row Multiple": (
                    "Row Multiple",
                    "1",
                    "Based on whether it matters the row on which you quit your stitch pattern. If your pattern has x rows and calls for repeating rows n through m, then your row_multiple is (m - n + 1). If it does not matter where you end the pattern and bind off, then enter 1. This value is always a whole number."
                ),
                "Row Remainder": (
                    "Row Remainder",
                    "0",
                    "Based on whether it matters the row on which you quit your stitch pattern. If your pattern has x rows and calls for repeating rows n through m, then your row_remainder is (x - m + n - 1).  If it does not matter where you end the pattern and bind off, then enter 0. This value is always a whole number."
                )
            }
        }

        gen = GenerateWidgets()
        layout, text_inputs, self.result_label = gen.generate_number_form(
            layout = layout,
            input_fields = input_fields,
            styles=style,
            submit_handler=self.submit,
        )

        self.start_width_input = text_inputs['start_width_input']
        self.end_width_input = text_inputs['end_width_input']
        self.length_input = text_inputs['length_input']
        self.gauge_width_input = text_inputs['gauge_width_input']
        self.gauge_length_input = text_inputs['gauge_length_input']
        self.pattern_inputs = []
        self.pattern_inputs.append(text_inputs['Stitch Multiple'])
        self.pattern_inputs.append(text_inputs['Stitch Remainder'])
        self.pattern_inputs.append(text_inputs['Row Multiple'])
        self.pattern_inputs.append(text_inputs['Row Remainder'])

        # should be the last widgets added
        self.add_widget(layout)
        self.add_widget(nav_drawer)

    def calc_screen(self, *args):
        self.manager.current='stitch_calc'
    def help_screen(self, *args):
        self.manager.current='help'
    def home_screen(self, *args):
        self.manager.current='home'
    def visual_screen(self, *args):
        self.manager.current='visualizer'
    def changewidth_screen(self, *args):
        self.manager.current='ChangeWidthPage'
    def resource_screen(self, *args):
        self.manager.current= 'resources'

    def submit(self, instance):
        # make sure tha user can't put in empty values
        float_check = [self.start_width_input.text, self.end_width_input.text, 
                       self.length_input.text, self.gauge_length_input.text, 
                       self.gauge_width_input.text]
        msg=[]
        for input_field in self.pattern_inputs:
            float_check.append(input_field.text)
        for input in float_check:
            if(self.sc.isValid(input,"int",msg) == True or self.sc.isValid(input,"float",msg) == True):
                continue
            else:
                self.result_label.text=msg[0]
                return
            
        # Capture all inputs into a dictionary
        outputs = {
            "Starting Width": float(self.start_width_input.text),
            "Ending Width": float(self.end_width_input.text),
            "Length": float(self.length_input.text),
            "Gauge Width": float(self.gauge_width_input.text),
            "Gauge Length": float(self.gauge_length_input.text),
            "Patterns": {f"Pattern {chr(65 + i)}": input_field.text for i, input_field in
                        enumerate(self.pattern_inputs)}
        }

        self.sc.setpattern(float(self.pattern_inputs[0].text),  # Sets Pattern restrictions for stitch calculator
                        float(self.pattern_inputs[1].text),
                        float(self.pattern_inputs[2].text),
                        float(self.pattern_inputs[3].text), )

        result = self.sc.change_width_calculator(float(self.start_width_input.text),
                                            float(self.end_width_input.text),
                                            float(self.length_input.text),
                                            float(self.gauge_width_input.text),
                                            float(self.gauge_length_input.text),
                                            )
        # Format the output
        cast_on, cast_off, row_count, adjustments = result  # Unpack the result
        formatted_result = f"[b]Cast on #[/b]: {cast_on} [b]Cast off #[/b]: {cast_off} [b]Total Row Count:[/b] {row_count}\n"


        # Add "Row number count" header only if adjustments are not empty
        if adjustments:
            formatted_result += "[b]Row number count:[/b]\n"
    
            # DEBUG: Print adjustments to inspect its contents
            print("DEBUG: adjustments =", adjustments)

        # Iterate through the adjustments to format each row increase/decrease
            for row, change in adjustments.items():
                if isinstance(row, int) and isinstance(change, (int, float)):  # Ensure valid data types
                    formatted_result += f"    • Row #{row}: [i]increase/decrease by {change}[/i]\n"

        # Display the formatted result in the result label with markup enabled
        self.result_label.markup = True
        self.result_label.text = formatted_result

        # Reset input fields
        self.end_width_input.text = ""
        self.start_width_input.text = ""
        self.length_input.text = ""
        self.gauge_width_input.text = ""
        self.gauge_length_input.text = ""
        for input_field in self.pattern_inputs:
            input_field.text = ""

        ##self.result_label.text = str(result)


class StitchNicheApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ChangeWidthPage(name='ChangeWidthPage'))    
        return sm

if __name__ == '__main__':
    StitchNicheApp().run()