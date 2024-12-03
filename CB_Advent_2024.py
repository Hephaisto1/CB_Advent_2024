from kivy.app import App
from kivy.uix.label import Label

class BlobApp(App):

    def build(self):
        return Label(text="Hello World")

if __name__ == "__main__":
    BlobApp().run()
