from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.storage.dictstore import DictStore



class Window(App):

    def build(self):
        self.store = DictStore('Data_CB_advent2024.py')
        self.input_field = BoxLayout(orientation="vertical")
        if len(self.store.keys()) == 0:
            self.text_name = TextInput(background_color="white",
                                   foreground_color="black",
                                   hint_text="Please enter your Name:",
                                   multiline=False)
            self.text_age = TextInput(background_color="white",
                                      foreground_color="black",
                                      hint_text="Please enter your Age:",
                                      multiline=False)
            self.text_adress = TextInput(background_color="white",
                                         foreground_color="black",
                                         hint_text="Please enter your Adress:",
                                         multiline=False)
        else:
            self.text_name = TextInput(background_color="white",
                                       foreground_color="black",
                                       hint_text="Please enter your Name:",
                                       multiline=False,
                                       text=self.store.get("person_data")["name"])
            self.text_age = TextInput(background_color="white",
                                      foreground_color="black",
                                      hint_text="Please enter your Age:",
                                      multiline=False,
                                      text=self.store.get("person_data")["age"])
            self.text_adress = TextInput(background_color="white",
                                         foreground_color="black",
                                         hint_text="Please enter your Adress:",
                                         multiline=False,
                                         text=self.store.get("person_data")["adress"])
        self.text_name.bind(on_text_validate=self.name_validation)
        self.text_age.bind(on_text_validate=self.age_validation)
        self.text_adress.bind(on_text_validate=self.adress_validation)
        self.text_name.bind(on_text_validate=self.data_storage)
        self.text_age.bind(on_text_validate=self.data_storage)
        self.text_adress.bind(on_text_validate=self.data_storage)
        self.input_field.add_widget(self.text_name)
        self.input_field.add_widget(self.text_age)
        self.input_field.add_widget(self.text_adress)
        return self.input_field

    def name_validation(self, *args):
        if self.text_name.text.isalpha() or self.text_name.text == " ":
            self.text_name.background_color = "white"
        else:
            self.text_name.background_color = "red"

    def age_validation(self, *args):
        if self.text_age.text.isdigit() and int(self.text_age.text) > 2 and int(self.text_age.text) < 100:
            self.text_age.background_color = "white"
        else:
            self.text_age.background_color = "red"

    def adress_validation(self, *args):
        if self.text_adress.text.isalnum() or self.text_name.text == " ":
            self.text_adress.background_color = "white"
        else:
            self.text_adress.background_color = "red"

    def data_storage(self, *args):
        self.store.put("person_data", name=self.text_name.text, age=self.text_age.text, adress=self.text_adress.text)
        print(self.store.get("person_data"))


if __name__ == '__main__':
    Window().run()
