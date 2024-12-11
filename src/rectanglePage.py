from email.quoprimime import header_decode
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from utils import Styles
# Import the StitchCalculator class
from utils import StitchCalculator
from utils import GenerateWidgets

# Import the StitchCalculator class
from utils import StitchCalculator
from help_page import HelpCenterScreen
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch') # remove red dots on ctrl-click

# Set the background color to white
Window.clearcolor = (1, 1, 1, 1)  # RGBA

class Rectangle(Screen):
    def __init__(self, **kwargs):
        super(Rectangle,self).__init__(**kwargs)
        from homePage import NavDrawer
        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)
        nav_drawer = NavDrawer(self)

        # nav_bar handles nav_drawer
        nav_bar = MDTopAppBar(title="Rectangle Calculator",md_bg_color=(0.5, 0, 0.5, 1))
        # opens nav_drawer on click
        nav_bar.left_action_items = [["menu", lambda x: nav_drawer.set_state("toggle")]]
        layout.add_widget(nav_bar)

        self.sc = StitchCalculator()

        style = Styles(
            label_color=(0.5, 0, 0.5, 1),
            header_color=(0.8, 0, 0.1),
            size_hint=(1, 1),
            height=35,
            background_color=(1, 1, 1, 1),
            padding=5,
            spacing=20
        )
        input_fields = {
            "Project measurements:": {  # header
                "width_input": (  # variable associated with input
                    "Width Input",  # label text for input
                    "8.0",  # default value
                    "How wide you want your finished piece to be. Can be entered as a decimal or whole number."
                # tooltip
                ),
                "length_input": (
                    "Length Input",
                    "60.0",
                    "How long you want your finished piece to be. Can be entered as a decimal or whole number."
                ),
                "gauge_width_input": (
                    "Gauge Width Input",
                    "7.14",
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
            layout=layout,
            input_fields=input_fields,
            styles=style,
            submit_handler=self.submit,
        )
        self.width_input = text_inputs['width_input']
        self.length_input = text_inputs['length_input']
        self.gauge_width_input = text_inputs['gauge_width_input']
        self.gauge_length_input = text_inputs['gauge_length_input']
        self.pattern_inputs = []
        self.pattern_inputs.append(text_inputs['Stitch Multiple'])
        self.pattern_inputs.append(text_inputs['Stitch Remainder'])
        self.pattern_inputs.append(text_inputs['Row Multiple'])
        self.pattern_inputs.append(text_inputs['Row Remainder'])

        self.add_widget(layout)
        self.add_widget(nav_drawer)
    
    def help_screen(self, *args):
        self.manager.current='help'
    def home_screen(self, *args):
        self.manager.current = 'home'
    def visual_screen(self, *args):
        self.manager.current='visualizer'
    def changewidth_screen(self, *args):
        self.manager.current='ChangeWidthPage'
    def resource_screen(self, *args):
        self.manager.current= 'resources'
    def rectangle_screen(self, *args):
        self.manager.current = 'rectangle'

    def submit(self, instance):
        # Capture all inputs into a dictionary
        outputs = {
            "Width": float(self.width_input.text),
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

        result = self.sc.rectangle_calculator(float(self.width_input.text),
                                              float(self.length_input.text),
                                              float(self.gauge_width_input.text),
                                              float(self.gauge_length_input.text),
                                              )

        # Print or process the outputs as needed (for demonstration)
        # print(outputs)  # You can remove this line later
        # Refresh the app by resetting input fields
        self.width_input.text = ""
        self.length_input.text = ""
        self.gauge_width_input.text = ""
        self.gauge_length_input.text = ""
        for input_field in self.pattern_inputs:
            input_field.text = ""

        self.result_label.text = str(result)

class Screens(ScreenManager):
    def __init__(self, **kwargs):
        super(Screens, self).__init__(**kwargs)
        # first Screen added is set as the current Screen
        self.add_widget(Rectangle(name='rectangle'))
        self.add_widget(HelpCenterScreen(name='help'))
class StitchNicheApp(MDApp):
    def build(self):
        # return Stitch_Calc()
        return Screens()


if __name__ == "__main__":
    StitchNicheApp().run()
