from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivymd.app import MDApp
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from help_page import HelpCenterScreen, PatternScreen
from stitchniche_gui import Stitch_Calc
from patternVisualizerPage import PatternVisuals
from changewidthpage import ChangeWidthPage
from resourcespage import ResourcesScreen
# Set the background color to white
Window.clearcolor = (1, 1, 1, 1)  # RGBA

def MakeList(title,icon_name,press_action):
    list = OneLineIconListItem(text=title)
    list.add_widget(IconLeftWidget(icon=icon_name))
    list.on_press = press_action
    return list

def NavDrawer(s):
    # create nav_drawer
    nav_drawer= MDNavigationDrawer(size_hint_x=.3,md_bg_color=(0.5, 0, 0.5, 1))
    nav_layout = BoxLayout(orientation='vertical')

    # start of items in nav_drawer
    list = MakeList("Home", "home",s.home_screen)
    nav_layout.add_widget(list)

    list = MakeList("Help", "help-box",s.help_screen)
    nav_layout.add_widget(list)

    list = MakeList("Calculator", "calculator",s.calc_screen)
    nav_layout.add_widget(list)

    list = MakeList("Visualizer", "eye-outline",s.visual_screen)
    nav_layout.add_widget(list)

    list = MakeList("Change Width", "ruler", s.changewidth_screen)
    nav_layout.add_widget(list)

    list = MakeList("Resources", "book", s.resource_screen)
    nav_layout.add_widget(list)

    # end of items in nav_drawer

    # without this the list starts from bottom
    nav_layout.add_widget(Label())
    nav_drawer.add_widget(nav_layout)
    return nav_drawer

class Home(Screen):
    def __init__(self,**kwargs):
        super(Home, self).__init__(**kwargs)
        # parent
        layout = BoxLayout(orientation='vertical')

        # creates NavDrawer and fills it Screens
        nav_drawer = NavDrawer(self)
        # nav_bar handles nav_drawer
        nav_bar = MDTopAppBar(title="Home",md_bg_color=(0.5, 0, 0.5, 1))
        # opens nav_drawer on click
        nav_bar.left_action_items = [["menu", lambda x: nav_drawer.set_state("toggle")]]
        layout.add_widget(nav_bar)

        welcome_message = Label(text="Welcome to StitchNiche!",font_size='50sp',color=(0.5, 0, 0.5, 1))
        layout.add_widget(welcome_message)
        button_title = Label(text="I want help with ...", size_hint=(1,.1), font_size='25sp',color=(0.5, 0, 0.5, 1))
        layout.add_widget(button_title)

        # child: makes row for buttons
        container = BoxLayout(orientation='horizontal', spacing='100sp', padding='100sp')
        container.add_widget(Button(text='Crocheting',font_size='25sp', background_color=(0.5, 0, 0.5, 1),on_press=self.calc_screen))
        container.add_widget(Button(text='Knitting',font_size='25sp',background_color=(0.5, 0, 0.5, 1),on_press=self.calc_screen))

        layout.add_widget(container)
        layout.add_widget(Label())

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
        self.add_widget(PatternScreen(name='pattern'))
        self.add_widget(PatternVisuals(name='visualizer'))
        self.add_widget(ChangeWidthPage(name='ChangeWidthPage')) 
        self.add_widget(ResourcesScreen(name='resources'))


class StitchNicheApp(MDApp):
    def build(self):
        return Screens()

if __name__ == '__main__':
    StitchNicheApp().run()
