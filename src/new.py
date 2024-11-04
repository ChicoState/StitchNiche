from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
import random

class ColorGrid(GridLayout):  # ColorGrid is itself a GridLayout
    def __init__(self, **kwargs):
        super(ColorGrid, self).__init__(**kwargs)
        self.cols = 5  # Define the number of columns
        self.spacing = 5  # Optional: add some space between buttons
        self.padding = 10  # Optional: add padding around the grid

        # Create 25 buttons and add them directly to this GridLayout
        for _ in range(25):
            btn = Button(background_normal="", background_color=[1, 1, 1, 1])
            btn.bind(on_press=self.change_color)
            self.add_widget(btn)  # Add each button to the grid layout

    def change_color(self, instance):
        # Randomly generate a color and set it as the button's background color
        new_color = [random.random(), random.random(), random.random(), 1]
        instance.background_color = new_color

class ColorGridApp(App):
    def build(self):
        return ColorGrid()  # Return an instance of ColorGrid as the root widget

if __name__ == '__main__':
    ColorGridApp().run()