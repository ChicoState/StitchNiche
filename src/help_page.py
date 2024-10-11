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

Window.clearcolor = (1, 1, 1, 1)

class HelpCenterScreen(Screen):
    def __init__(self, **kwargs):
        super(HelpCenterScreen, self).__init__(**kwargs)
        from homePage import NavDrawer

        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)

        nav_drawer = NavDrawer(self)
        # nav_bar handles nav_drawer
        nav_bar = MDTopAppBar(title="StitchNiche Help Center",md_bg_color=(0.5, 0, 0.5, 1))
        # opens nav_drawer on click
        nav_bar.left_action_items = [["menu", lambda x: nav_drawer.set_state("toggle")]]
        layout.add_widget(nav_bar)

        # Adjusting banner size
        banner = BoxLayout(size_hint=(1, 0.15))
        with banner.canvas.before:
            Color(0.8, 0.6, 1, 1)
            self.banner_bg = Rectangle(pos=banner.pos, size=banner.size)
        banner.bind(pos=self.update_bg, size=self.update_bg)

        # Banner text
        banner_text = Label(text="StitchNiche Help Center", color=[1, 1, 1, 1], font_size='32sp', bold=True, size_hint=(1, 1))
        banner.add_widget(banner_text)
        layout.add_widget(banner)

        # Add buttons for each pattern type
        pattern_buttons = GridLayout(cols=1, spacing=10, size_hint_y=None)
        pattern_buttons.bind(minimum_height=pattern_buttons.setter('height'))
        
        # Pattern buttons
        patterns = [("Rectangle", "rectangle_helppage.txt"), ("Square", "square_helppage.txt"), 
                    ("Circle", "circle_helppage.txt"), ("Trapezoid", "trapezoid_helppage.txt")]

        for pattern, filename in patterns:
            btn = Button(text=pattern, size_hint_y=None, height=50, on_release=lambda btn, f=filename: self.load_pattern(f))
            pattern_buttons.add_widget(btn)

        scroll_view = ScrollView(size_hint=(1, 1))
        scroll_view.add_widget(pattern_buttons)
        layout.add_widget(scroll_view)

        self.add_widget(layout)
        self.add_widget(nav_drawer)
    def calc_screen(self, *args):
        self.manager.current='stitch_calc'
    def help_screen(self, *args):
        self.manager.current='help'
    def home_screen(self, *args):
        self.manager.current='home'
    def load_pattern(self, filename):
        # Switch to the pattern screen and load content from the selected file
        self.manager.current = 'pattern'
        self.manager.get_screen('pattern').load_content_from_file(filename)   

    def update_bg(self, instance, value):
        self.banner_bg.pos = instance.pos
        self.banner_bg.size = instance.size
 
class PatternScreen(Screen):
    def __init__(self, **kwargs):
        super(PatternScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)

        # ScrollView for the content
        self.scroll_view = ScrollView(size_hint=(1, 0.85))
        self.content_layout = GridLayout(cols=1, padding=10, spacing=20, size_hint_y=None)
        self.content_layout.bind(minimum_height=self.content_layout.setter('height'))
        self.scroll_view.add_widget(self.content_layout)
        layout.add_widget(self.scroll_view)

        # Add a back button
        back_button = Button(text="Back", size_hint_y=None, height=50)
        back_button.bind(on_release=self.go_back)
        layout.add_widget(back_button)
        self.add_widget(layout)

    def go_back(self, instance):
        # Switch back to the Help Center screen
        self.manager.current = 'help'

    def load_content_from_file(self, filename):
        # Clear existing content
        self.content_layout.clear_widgets()

        # Load content from the selected .txt file
        try:
            with open(filename, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            content = f"Error: Could not find the file '{filename}'."

        # Display the content
        content_label = Label(
            text=content,
            font_size='16sp',
            color=[0, 0, 0, 1],
            halign="left",
            valign="top",
            text_size=(Window.width - 40, None),  # Adjust width based on your layout
            size_hint_y=None,  # Allow height to be determined by content
    )
        content_label.bind(texture_size=content_label.setter('size'))  # Bind size to texture size
        
        # Optional: Add a maximum height to the label if needed
        content_label.height = max(content_label.height, 400)  # Minimum height for display

        self.content_layout.add_widget(content_label)

    def get_label_height(self, content):
    # Estimate the height of the label based on the number of lines
        line_height = 20  # Approximate height per line in pixels
        return line_height * content.count('\n') + 40
    

class StitchNicheApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HelpCenterScreen(name='help'))
        sm.add_widget(PatternScreen(name='pattern'))      
        return sm

if __name__ == '__main__':
    StitchNicheApp().run()