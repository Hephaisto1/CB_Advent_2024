from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput



class Window(App):

    def build(self):
        self.input_field = BoxLayout(orientation="vertical")
        self.text_name = TextInput(background_color="white",
                                   foreground_color="black",
                                   hint_text="Please enter your Name:",
                                   multiline=False)
        self.text_age = TextInput(background_color="white",
                                   foreground_color="black",
                                   hint_text="Please enter your Age:",
                                   multiline=False)
        self.text_adress = TextInput(background_color = "white",
                                     foreground_color = "black",
                                     hint_text = "Please enter your Adress:",
                                     multiline=False)
        self.text_name.bind(on_text_validate=self.name_validation)
        self.text_age.bind(on_text_validate=self.age_validation)
        self.text_adress.bind(on_text_validate=self.adress_validation)
        self.input_field.add_widget(self.text_name)
        self.input_field.add_widget(self.text_age)
        self.input_field.add_widget(self.text_adress)
        return self.input_field

    def name_validation(self, *args):
        if self.text_name.text.isalpha() or self.text_name.text == " ":
            pass
        else:
            self.text_name.background_color = "red"

    def age_validation(self, *args):
        if self.text_age.text.isdigit() and int(self.text_age.text) > 2 and int(self.text_age.text) < 100:
            pass
        else:
            self.text_age.background_color = "red"

    def adress_validation(self, *args):
        if self.text_adress.text.isalnum() or self.text_name.text == " ":
            pass
        else:
            self.text_adress.background_color = "red"


if __name__ == '__main__':
    Window().run()

"""
To Do's: Tag 5: Die Input-Felder so gestalten, dass bei einer erneuten Eingabe/korrekten Eingabe der rote Hintergrund verschwindet


"""