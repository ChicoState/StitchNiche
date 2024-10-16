from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from kivymd.app import MDApp

Window.clearcolor = (1, 1, 1, 1)

class PatternVisuals(Screen):
    def __init__(self, **kwargs):
        super(PatternVisuals, self).__init__(**kwargs)
        from homePage import NavDrawer
        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)
        nav_drawer = NavDrawer(self)
        # nav_bar handles nav_drawer
        nav_bar = MDTopAppBar(title="Visualizer",md_bg_color=(0.5, 0, 0.5, 1))
        # opens nav_drawer on click
        nav_bar.left_action_items = [["menu", lambda x: nav_drawer.set_state("toggle")]]
        layout.add_widget(nav_bar)


        layout.add_widget(Label(text="Output Here",color=(0.5, 0, 0.5, 1)))

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


class StitchNicheApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PatternVisuals(name='visualizer'))    
        return sm

if __name__ == '__main__':
    StitchNicheApp().run()