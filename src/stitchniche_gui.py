import os
import sys
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

# Set the background color to white
Window.clearcolor = (1, 1, 1, 1)  # RGBA

class StitchNicheApp(App):
    def build(self):
        # Main layout for the form
        layout = BoxLayout(orientation='vertical', padding=(20, 20, 20, 20), spacing=10)
        
        # Title
        title_label = Label(text="Stitch Niche", font_size='32sp', color=(0.5, 0, 0.5, 1))
        layout.add_widget(title_label)

        # Sub Title
        title_label = Label(text="Stitch Calculator - Rectangle", font_size='20sp', color=(0.5, 0, 0.5, 1))
        layout.add_widget(title_label)

        # Form layout
        form_layout = GridLayout(cols=2, padding=5, spacing=5, size_hint=(0.5, None))
        form_layout.bind(minimum_height=form_layout.setter('height'))  # Make it wrap content

        # Cast on Stitch Title
        form_layout.add_widget(Label(text="Cast on stitch #:", color=(0.8, 0, 0.1)))
        form_layout.add_widget(Label())  # Empty space for alignment

        # Width
        form_layout.add_widget(Label(text="Width (inches):", color=(0.5, 0, 0.5, 1)))
        self.width_input = TextInput(size_hint_y=None, height=35, background_color=(1, 1, 1, 1), 
                                      size_hint_x=0.5)
        form_layout.add_widget(self.width_input)

        # Length
        form_layout.add_widget(Label(text="Length (inches):", color=(0.5, 0, 0.5, 1)))
        self.length_input = TextInput(size_hint_y=None, height=35, background_color=(1, 1, 1, 1), 
                                       size_hint_x=0.5)
        form_layout.add_widget(self.length_input)

        # Gauge
        form_layout.add_widget(Label(text="Gauge Width (inches):", color=(0.5, 0, 0.5, 1)))
        self.gauge_width_input = TextInput(size_hint_y=None, height=35, background_color=(1, 1, 1, 1), 
                                            size_hint_x=0.5)
        form_layout.add_widget(self.gauge_width_input)

        form_layout.add_widget(Label(text="Gauge Length (inches):", color=(0.5, 0, 0.5, 1)))
        self.gauge_length_input = TextInput(size_hint_y=None, height=35, background_color=(1, 1, 1, 1), 
                                             size_hint_x=0.5)
        form_layout.add_widget(self.gauge_length_input)

        # Pattern Title
        form_layout.add_widget(Label(text="Pattern:", color=(0.8, 0, 0.1)))
        form_layout.add_widget(Label())  # Empty space for alignment

        # Pattern Inputs
        self.pattern_inputs = []
        for pattern in ['A', 'B', 'C', 'D']:
            form_layout.add_widget(Label(text=f"{pattern}:", color=(0.5, 0, 0.5, 1)))
            pattern_input = TextInput(size_hint_y=None, height=35, background_color=(1, 1, 1, 1), 
                                      size_hint_x=0.5)
            self.pattern_inputs.append(pattern_input)
            form_layout.add_widget(pattern_input)

        layout.add_widget(form_layout)

        # Submit Button
        submit_button = Button(text="Submit", size_hint=(None, 0.5), height=50)
        submit_button.bind(on_press=self.submit)
        layout.add_widget(submit_button)

        return layout

    def submit(self, instance):
        # Capture all inputs into a dictionary
        outputs = {
            "Width": self.width_input.text,
            "Length": self.length_input.text,
            "Gauge Width": self.gauge_width_input.text,
            "Gauge Length": self.gauge_length_input.text,
            "Patterns": {f"Pattern {chr(65+i)}": input_field.text for i, input_field in enumerate(self.pattern_inputs)}
        }

        # Print or process the outputs as needed (for demonstration)
        print(outputs)  # You can remove this line later
        # Refresh the app by resetting input fields
        self.width_input.text = ""
        self.length_input.text = ""
        self.gauge_width_input.text = ""
        self.gauge_length_input.text = ""
        for input_field in self.pattern_inputs:
            input_field.text = ""

if __name__ == "__main__":
    StitchNicheApp().run()


