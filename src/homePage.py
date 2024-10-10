from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from help_page import HelpCenterScreen
from stitchniche_gui import Stitch_Calc

# Set the background color to white
Window.clearcolor = (1, 1, 1, 1)  # RGBA

class Home(Screen):
    def __init__(self,**kwargs):
        super(Home, self).__init__(**kwargs)
        # parent
        layout = BoxLayout(orientation='vertical')
        welcome_message = Label(text="Welcome to StitchNiche!",font_size='50sp',color=(0.5, 0, 0.5, 1))
        layout.add_widget(welcome_message)
        button_title = Label(text="I want help with ...", size_hint=(1,.1), font_size='25sp',color=(0.5, 0, 0.5, 1))
        layout.add_widget(button_title)

        # child: makes row for buttons
        container = BoxLayout(orientation='horizontal', spacing='100sp', padding='100sp')
        container.add_widget(Button(text='Crocheting',font_size='25sp', background_color=(0.5, 0, 0.5, 1),on_press=self.switch_screen))
        container.add_widget(Button(text='Knitting',font_size='25sp',background_color=(0.5, 0, 0.5, 1),on_press=self.switch_screen))

        layout.add_widget(container)
        layout.add_widget(Label())

        self.add_widget(layout)
    
    def switch_screen(self, *args):
        self.manager.current = 'stitch_calc'

""" in order to create a new Screen you need to (in a new .py file):
        1. include
            from kivy.uix.screenmanager import Screen
        2. create a class and give it the parameter 'Screen'
            ex. class <name>(Screen):
        2. in declaration use
            def __init__(self, **kwargs):
                super(<class name>, self).__init__(**kwargs)
        3. add your layout using 
            self.add_widget(<layout name>)
            (this should be last line; nothing is returned)
        4. on this page 
            from <.py file name> import <class name>
"""
# instantiate Screens here
class Screens(ScreenManager):
    def __init__(self, **kwargs):
        super(Screens, self).__init__(**kwargs)
        # first Screen added is set as the current Screen
        self.add_widget(Home(name='home'))
        self.add_widget(Stitch_Calc(name='stitch_calc'))
        self.add_widget(HelpCenterScreen(name='help'))


class StitchNicheApp(App):
    def build(self):
        return Screens()

if __name__ == '__main__':
    StitchNicheApp().run()
