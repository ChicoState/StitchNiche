from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.toolbar import MDTopAppBar
from kivy.core.window import Window
from kivymd.app import MDApp

from utils import PatternVisualizer  # Import PatternVisualizer from utils

Window.clearcolor = (1, 1, 1, 1)

class PatternVisuals(Screen):
    def __init__(self, **kwargs):
        super(PatternVisuals, self).__init__(**kwargs)
        from homePage import NavDrawer  # Ensure NavDrawer is available

        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)

        # Navigation Drawer and Toolbar
        nav_drawer = NavDrawer(self)
        nav_bar = MDTopAppBar(title="Visualizer", md_bg_color=(0.5, 0, 0.5, 1))
        nav_bar.left_action_items = [["menu", lambda x: nav_drawer.set_state("toggle")]]
        layout.add_widget(nav_bar)

        # Define initial matrix and color map for PatternVisualizer
        initial_matrix = [[0 for _ in range(5)] for _ in range(5)]
        color_value_map = {
            -1: ("Purl", [0.7, 0.7, 1, 1]),   # Light Blue
             0: ("No Stitch", [1, 1, 1, 1]),  # White
             1: ("Knit", [0, 0, 0.5, 1])      # Dark Blue
        }

        # Add PatternVisualizer (includes matrix and legend)
        self.pattern_visualizer = PatternVisualizer(initial_matrix, color_value_map)
        layout.add_widget(self.pattern_visualizer)

        # Add a Save button below the PatternVisualizer
        save_button = Button(text="Save", size_hint_y=0.1)
        save_button.bind(on_press=self.save_matrix)
        layout.add_widget(save_button)

        # Finalize layout
        self.add_widget(layout)
        self.add_widget(nav_drawer)

    def save_matrix(self, instance):
        # Retrieve the updated matrix from PatternVisualizer
        matrix = self.pattern_visualizer.get_matrix()
        self.save_handler(matrix)

    def save_handler(self, matrix):
        # Placeholder for the save functionality
        print("Matrix saved:", matrix)

    # Screen navigation methods
    def calc_screen(self, *args):
        self.manager.current = 'stitch_calc'

    def help_screen(self, *args):
        self.manager.current = 'help'

    def home_screen(self, *args):
        self.manager.current = 'home'

    def visual_screen(self, *args):
        self.manager.current = 'visualizer'


class StitchNicheApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(PatternVisuals(name='visualizer'))
        return sm


if __name__ == '__main__':
    StitchNicheApp().run()
