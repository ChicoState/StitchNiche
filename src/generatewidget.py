import os
import sys
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from utils import Styles
# Import the StitchCalculator class
from utils import StitchCalculator
from utils import GenerateWidgets

# Set the background color to white
Window.clearcolor = (1, 1, 1, 1)  # RGBA


class StitchNicheApp(App):
    def build(self):
        self.sc = StitchCalculator()
        # Main layout for the form
        layout = BoxLayout(orientation='vertical', spacing=30, size_hint=(1, 1))

        # Title
        # GenerateFormKivy.form({"input 1" : 0.0,
        #                 "input 2" : "inches",}, styles = )
        title_label = Label(text="Stitch Niche", font_size='32sp', color=(0.5, 0, 0.5, 1))
        layout.add_widget(title_label)

        # Sub Title
        title_label = Label(text="Stitch Calculator - Rectangle", font_size='20sp', color=(0.5, 0, 0.5, 1))
        layout.add_widget(title_label)

        # Form layout

        style = Styles(color=(0.5, 0, 0.5, 1), size_hint=(0.90, None), height=35, background_color=(1, 1, 1, 1), padding=5, spacing=20)
        input_label = ["width_input", "length_input", "gauge_width_input", "gauge_length_input", "a", "b", "c", "d"]
        gen = GenerateWidgets()
        layout, text_inputs, self.result_label = gen.generate_number_form(cols = 2, layout = layout, labels = input_label, styles=style, submit_handler=self.submit)
        self.width_input = text_inputs['width_input']
        self.length_input = text_inputs['length_input']
        self.gauge_width_input = text_inputs['gauge_width_input']
        self.gauge_length_input = text_inputs['gauge_length_input']
        self.pattern_inputs = []
        self.pattern_inputs.append(text_inputs['a'])
        self.pattern_inputs.append(text_inputs['b'])
        self.pattern_inputs.append(text_inputs['c'])
        self.pattern_inputs.append(text_inputs['d'])


        return layout

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

        result = self.sc.rectangle_calculator(float(self.width_input.text),
                                              float(self.length_input.text),
                                              float(self.gauge_width_input.text),
                                              float(self.gauge_length_input.text),
                                              float(self.pattern_inputs[0].text),
                                              float(self.pattern_inputs[1].text),
                                              float(self.pattern_inputs[2].text),
                                              float(self.pattern_inputs[3].text), )

        # Print or process the outputs as needed (for demonstration)
        print(outputs)  # You can remove this line later
        # Refresh the app by resetting input fields
        self.width_input.text = ""
        self.length_input.text = ""
        self.gauge_width_input.text = ""
        self.gauge_length_input.text = ""
        for input_field in self.pattern_inputs:
            input_field.text = ""

        self.result_label.text = str(result);


if __name__ == "__main__":
    StitchNicheApp().run()


