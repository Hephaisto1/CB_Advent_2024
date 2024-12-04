from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class LoginScreen(App):
    def build(self):
        b = BoxLayout(orientation="vertical")
        text_name = TextInput()
        text_age = TextInput()
        text_adress = TextInput()
        label_name = Label(text = "Name: ")
        label_age = Label(text = "Age: ")
        label_adress = Label(text = "Adress: ")
        b.add_widget(label_name)
        b.add_widget(text_name)
        b.add_widget(label_age)
        b.add_widget(text_age)
        b.add_widget(label_adress)
        b.add_widget(text_adress)
        return b


if __name__ == '__main__':
    LoginScreen().run()
