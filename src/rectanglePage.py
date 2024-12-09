import os
import sys
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivymd.uix.toolbar import MDTopAppBar
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp

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

        # layout body
        layout.add_widget(Label()) # temp; delete when more widgets added

        self.add_widget(layout)
        self.add_widget(nav_drawer)
    
    def calc_screen(self, *args):
        self.manager.current='stitch_calc'
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
