from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

# Here is a comment
class StichNicheApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')

        label1 = Label(text="Hello World")
        label2 = Label(text="Button2")
        layout.add_widget(label1)
        layout.add_widget(label2)

        return layout

if __name__ == '__main__':
    StichNicheApp().run()