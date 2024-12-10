from kivymd.uix.screen import Screen
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.navigationdrawer import MDNavigationDrawer
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivymd.app import MDApp
import webbrowser
import os
import requests
from patternVisualizerPage import PatternVisuals
from kivy.config import Config
Config.set('input', 'mouse', 'mouse,disable_multitouch') # remove red dots on ctrl-click

class ResourcesScreen(Screen):
    def __init__(self, **kwargs):
        super(ResourcesScreen, self).__init__(**kwargs)
        from homePage import NavDrawer # placing imports here avoid circular dependencies 

        # Main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=20)

        # Navigation Drawer
        nav_drawer = NavDrawer(self)
        # nav_bar handles nav_drawer
        nav_bar = MDTopAppBar(title="Resources",md_bg_color=(0.5, 0, 0.5, 1))
        # opens nav_drawer on click
        nav_bar.left_action_items = [["menu", lambda x: nav_drawer.set_state("toggle")]]
        layout.add_widget(nav_bar)


        # Banner
        banner = BoxLayout(size_hint=(1, 0.15))
        with banner.canvas.before:
            Color(0.8, 0.6, 1, 1)
            self.banner_bg = Rectangle(pos=banner.pos, size=banner.size)
        banner.bind(pos=self.update_bg, size=self.update_bg)


        # ScrollView for video resources
        scroll_view = ScrollView(size_hint=(1, 1))
        video_layout = GridLayout(cols=1, spacing=20, padding=10, size_hint_y=None)
        video_layout.bind(minimum_height=video_layout.setter('height'))

        # Define the video resources
        videos = [
            {
                "title": "What's the Difference Between Knitting and Crochet",
                "thumbnail_url": "https://img.youtube.com/vi/m2Ky76O116A/0.jpg",
                "video_url": "https://www.youtube.com/watch?v=m2Ky76O116A"
            },
            {
                "title": "The (Almost) Ultimate Guide on Knitting for Beginners",
                "thumbnail_url": "https://img.youtube.com/vi/m1FbeAvBrVE/0.jpg",
                "video_url": "https://www.youtube.com/watch?v=m1FbeAvBrVE&t=190s"
            },
            {
                "title": "Introduction to Gauge in Knitting",
                "thumbnail_url": "https://img.youtube.com/vi/FckfIcDU52o/0.jpg",
                "video_url": "https://www.youtube.com/watch?v=FckfIcDU52o"
            },
            {
                "title": "How to Change a Knitting Pattern to a New Gauge",
                "thumbnail_url": "https://img.youtube.com/vi/q3kf8aFDSFE/0.jpg",
                "video_url": "https://www.youtube.com/watch?v=q3kf8aFDSFE"
            },
            {
                "title": "How to Knit The Purl Stitch for Beginners",
                "thumbnail_url": "https://img.youtube.com/vi/zPwR2tYQWBY/0.jpg",
                "video_url": "https://www.youtube.com/watch?v=zPwR2tYQWBY"
            },                      
            {            
                "title": "Moss Stitch Rectangle - NO Twisting NO Jogs",
                "thumbnail_url": "https://img.youtube.com/vi/ou8ADtFot40/0.jpg",
                "video_url": "https://www.youtube.com/watch?v=ou8ADtFot40"
            }
        ]


        for video in videos:
            image_path = self.download_image(video["thumbnail_url"], video["title"])
            if image_path:
                # Layout for each video
                video_box = BoxLayout(orientation='vertical', size_hint_y=None, height=400, padding=10, spacing=10)

                # Title button
                title_button = Button(
                    text=video["title"],
                    size_hint=(None, None),
                    width=400,
                    height=40,
                    font_size=16,
                    text_size=(350, None),
                    halign="center",
                    valign="middle",
                    background_normal='',
                    background_color=(0.5, 0, 0.5, 1)
                )
                title_button.bind(on_release=lambda instance, url=video["video_url"]: webbrowser.open(url))

                # Thumbnail image
                thumbnail = Image(source=image_path, size_hint=(None,None), height=300, width=400)

                # Add to video layout
                video_box.add_widget(title_button)
                video_box.add_widget(thumbnail)

                # Add video layout to main video layout
                video_layout.add_widget(video_box)

        # Add video layout to ScrollView
        scroll_view.add_widget(video_layout)
        layout.add_widget(scroll_view)

        self.add_widget(layout)
        self.add_widget(nav_drawer)


    def download_image(self, url, title):
        """Download an image from the given URL and save it locally."""
        try:
            # Create a unique filename for the image
            filename = f"{title.replace(' ', '_')}.jpg"
            # Save to the current working directory
            filepath = os.path.join(os.getcwd(), filename)
            
            # Download the image only if it doesn't already exist locally
            if not os.path.exists(filepath):
                response = requests.get(url)
                response.raise_for_status()  # Check for download errors

                with open(filepath, "wb") as file:
                    file.write(response.content)
                print(f"Downloaded image for {title} to {filepath}")
            else:
                print(f"Image already exists for {title}")

            return filepath
        except Exception as e:
            print(f"Error downloading image: {e}")
            return None

        
    def update_bg(self, instance, value):
        if hasattr(self, 'banner_bg'):
            self.banner_bg.pos = instance.pos
            self.banner_bg.size = instance.size

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

class StitchNicheApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(ResourcesScreen(name='resources'))    
        return sm

if __name__ == '__main__':
    StitchNicheApp().run()