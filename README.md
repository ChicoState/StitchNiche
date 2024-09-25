[Where I got environment setup from](https://www.youtube.com/watch?v=LRXo0juuTrw&t)

# Downloading the Repo
When you download this repo, make sure you to put it in your PyCharmProjects folder. On Windows, it should be located in `C:\Users\***YOUR USERNAME***\PycharmProjects`

# Initializing a new project steps:

1. Download Python 3.9. Use the Microsoft Store if you are using Windows.
2. Check that you have properly downloaded it by running python --version. If it doesn't appear, make sure you have added the Python bin directory to your path. Here is a video on how to do that: https://www.geeksforgeeks.org/how-to-add-python-to-windows-path/
3. Download Pycharm. When you are installing it, make sure to check the "add bin to Path".
4. Create a new Pycharm project. Select Python 3.9 as your interpreter. If it doesn't appear there, restart your machine and/or check previous step.
5. Go to File/Settings/Project:[YOURPYCHARMPROJECTNAME]/Python Interpreter. This will open a new tab. Click the small + icon and add the following packages (make sure to click the 'specify version' and ensure you are choosing the versions listed below):
- Kivy 2.3.0
- kivymd 1.2.0
- pandas 2.2.3
- numpy 2.1.1
6. You can now start coding using Kivy. Here is the starter code:
```
from kivymd.app import MDApp

class StichNicheApp(MDApp):
    def build(self):
        return

StichNicheApp().run()
```
