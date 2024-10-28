from kivy.app import App 
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.dropdown import DropDown
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivymd.uix.toolbar import MDTopAppBar
from kivy.core.window import Window
from kivymd.app import MDApp

#from utils import put_to_screen

Window.clearcolor = (1, 1, 1, 1)

class PatternVisuals(Screen):
    def __init__(self, **kwargs):
        super(PatternVisuals, self).__init__(**kwargs)
        from homePage import NavDrawer
        
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=50)
        self.nav_drawer = NavDrawer(self)  # Create the nav drawer instance, but don't add it yet
        
        # Navigation bar
        nav_bar = MDTopAppBar(title="Visualizer", md_bg_color=(0.5, 0, 0.5, 1))
        nav_bar.left_action_items = [["menu", self.toggle_nav_drawer]]  # Set the toggle function for the menu button
        layout.add_widget(nav_bar)

        # Adjusting banner size
        banner = BoxLayout(size_hint=(1, 0.15))
        with banner.canvas.before:
            Color(0.8, 0.6, 1, 1)
            self.banner_bg = Rectangle(pos=banner.pos, size=banner.size)
        banner.bind(pos=self.update_bg, size=self.update_bg)

        # Centering layout for buttons
        button_layout = GridLayout(cols=1, spacing=30, size_hint_y=None)
        button_layout.bind(minimum_height=button_layout.setter('height'))

        # Dropdown for pattern selection
        self.dropdown = DropDown()
        self.pattern_button = Button(text='Select Pattern', size_hint_y=None, height=80)

        # Sample patterns (replace with your actual saved patterns)
        patterns = ['Pattern 1', 'Pattern 2', 'Pattern 3']  
        for pattern in patterns:
            btn = Button(text=pattern, size_hint_y=None, height=40)
            btn.bind(on_release=lambda btn: self.dropdown.select(btn.text))
            self.dropdown.add_widget(btn)

        # Bind dropdown selection to button text
        self.pattern_button.bind(on_release=self.dropdown.open)
        self.dropdown.bind(on_select=lambda instance, x: setattr(self.pattern_button, 'text', x))

        # Add dropdown button to the button layout
        button_layout.add_widget(self.pattern_button)

        # Load button to show selected pattern
        load_button = Button(text='Load Pattern', size_hint_y=None, height=80)
        load_button.bind(on_release=self.load_pattern)

        # Add load button to button layout
        button_layout.add_widget(load_button)

        # Output label below the buttons
        self.output_label = Label(text="Output Here", color=(0.5, 0, 0.5, 1), size_hint_y=None, height=40)
        button_layout.add_widget(self.output_label)

        # Add scroll view to allow for additional buttons if needed
        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(button_layout)

        # Add the scroll view to the main layout
        layout.add_widget(scroll_view)

        # Add the main layout to the screen
        self.add_widget(layout)

    def toggle_nav_drawer(self):
        if self.nav_drawer.parent:
            self.remove_widget(self.nav_drawer)  # Hide the nav drawer if it is currently displayed
        else:
            self.add_widget(self.nav_drawer)  # Show the nav drawer if it is hidden

    def load_pattern(self, instance):
        selected_pattern = self.pattern_button.text
        # Update the output label with the selected pattern
        self.output_label.text = f"Loading pattern: {selected_pattern}"

    def update_bg(self, instance, value):
        self.banner_bg.pos = instance.pos
        self.banner_bg.size = instance.size

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

