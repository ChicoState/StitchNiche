from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, Rectangle

Window.clearcolor = (1, 1, 1, 1)  # RGBA

class HelpCenterScreen(Screen):
    def __init__(self, **kwargs):
        super(HelpCenterScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)

        # Create the banner with a light purple background
        banner = BoxLayout(size_hint=(1, 0.10))  # Adjusted height for the banner
        with banner.canvas.before:
            Color(0.8, 0.6, 1, 1)  # Light purple color
            banner_bg = Rectangle(pos=banner.pos, size=banner.size)

        # Bind size and position to dynamically update banner background
        banner.bind(pos=lambda instance, value: setattr(banner_bg, 'pos', value),
                    size=lambda instance, value: setattr(banner_bg, 'size', value))

        # Add text label to the banner
        banner_text = Label(text="StitchNiche Help Center", 
                            color=[1, 1, 1, 1],  # White text color
                            font_size='28sp',
                            bold=True,
                            halign='left',
                            valign='middle',
                            size_hint_x=None,  # Set size_hint_x to None to control the width
                            width=400)  # Set an explicit width for the label)
        banner.add_widget(banner_text)

        # Add the banner to the layout
        layout.add_widget(banner)

        # Centered heading message - reduced spacing from the banner
        heading = Label(text="We Are Here To Help", bold=True, font_size='30sp', color=(0.1, 0.1, 0.1, 1), halign='center', valign='top', size_hint_y=None, height=40)
        heading.bind(size=heading.setter('text_size'))  # Ensure text is centered inside the label
        layout.add_widget(heading)

        layout.add_widget(Label())  # Empty space for future content

        self.add_widget(layout)

class StitchNicheApp(App):
    def build(self):
        # Screen Manager
        sm = ScreenManager()

        # Adding the Help Page Screen
        help_screen = HelpCenterScreen(name='help')
        sm.add_widget(help_screen)

        return sm


if __name__ == '__main__':
    StitchNicheApp().run()