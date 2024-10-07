from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.button import Button

# Set the background color to white
Window.clearcolor = (1, 1, 1, 1)  # RGBA

# Here is a comment
class StitchNicheApp(App):
    def build(self):
        # parent
        layout = BoxLayout(orientation='vertical')
        welcome_message = Label(text="Welcome to StitchNiche!",font_size='50sp',color=(0.5, 0, 0.5, 1))
        layout.add_widget(welcome_message)
        button_title = Label(text="I want help with ...", size_hint=(1,.1), font_size='25sp',color=(0.5, 0, 0.5, 1))
        layout.add_widget(button_title)

        # child: makes row for buttons
        container = BoxLayout(orientation='horizontal', spacing='100sp', padding='100sp')
        container.add_widget(Button(text='Crocheting',font_size='25sp', background_color=(0.5, 0, 0.5, 1)))
        container.add_widget(Button(text='Knitting',font_size='25sp',background_color=(0.5, 0, 0.5, 1)))

        layout.add_widget(container)
        layout.add_widget(Label())



        return layout

if __name__ == '__main__':
    StitchNicheApp().run()
