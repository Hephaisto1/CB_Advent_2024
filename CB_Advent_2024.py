from kivy.app import App
from kivy.uix.label import Label

class BlobApp(App):

    def build(self):
        return Label(text="Hello World")

#This comment is new and should change the version of the file

if __name__ == "__main__":
    BlobApp().run()
