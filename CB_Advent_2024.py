from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.storage.dictstore import DictStore
from kivy.uix.button import Button

class Christmas(App):

    def build(self):
        self.field_counter = 0
        self.store = DictStore('Data_CB_advent2024.py')
        self.input_field = RelativeLayout()
        if len(self.store.keys()) == 0:
            self.text_name = TextInput(background_color="white",
                                       foreground_color="black",
                                       hint_text="Please enter your Name:",
                                       multiline=False,
                                       size_hint=(1,0.15),
                                       pos_hint={"x":0.0,"y":0.85})
            self.text_age = TextInput(background_color="white",
                                      foreground_color="black",
                                      hint_text="Please enter your Age:",
                                      multiline=False,
                                      size_hint=(1, 0.15),
                                      pos_hint={"x":0.0,"y":0.7}
                                      )
            self.text_adress = TextInput(background_color="white",
                                         foreground_color="black",
                                         hint_text="Please enter your Adress:",
                                         multiline=False,
                                         size_hint=(1, 0.15),
                                         pos_hint={"x":0.0,"y":0.55}
                                         )
        else:
            self.text_name = TextInput(background_color="white",
                                       foreground_color="black",
                                       hint_text="Please enter your Name:",
                                       multiline=False,
                                       text=self.store.get("person_data")["name"],
                                       size_hint=(1, 0.15),
                                       pos_hint={"x":0.0,"y":0.85}
                                       )
            self.text_age = TextInput(background_color="white",
                                      foreground_color="black",
                                      hint_text="Please enter your Age:",
                                      multiline=False,
                                      text=self.store.get("person_data")["age"],
                                      size_hint=(1, 0.15),
                                      pos_hint={"x":0.0,"y":0.7}
                                      )
            self.text_adress = TextInput(background_color="white",
                                         foreground_color="black",
                                         hint_text="Please enter your Adress:",
                                         multiline=False,
                                         text=self.store.get("person_data")["adress"],
                                         size_hint=(1, 0.15),
                                         pos_hint={"x":0.0,"y":0.55}
                                         )
        self.button_add = Button(text="Add",size_hint=(1, 0.25),pos_hint={"x":0.0,"y":0.0})
        self.text_name.bind(on_text_validate=self.name_validation)
        self.text_age.bind(on_text_validate=self.age_validation)
        self.text_adress.bind(on_text_validate=self.adress_validation)
        self.text_name.bind(on_text_validate=self.data_storage)
        self.text_age.bind(on_text_validate=self.data_storage)
        self.text_adress.bind(on_text_validate=self.data_storage)
        self.input_field.add_widget(self.text_name)
        self.input_field.add_widget(self.text_age)
        self.input_field.add_widget(self.text_adress)
        self.button_add.bind(on_press=self.add_field_description)
        self.input_field.add_widget(self.button_add)
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

    def add_field_description(self, *args):
        if self.field_counter == 0:
            self.item_description = Label(color="white",
                                          size_hint=(0.5, 0.15),
                                          pos_hint={"x": 0.0, "y": 0.4}
                                          )
            self.item_field = TextInput(background_color="white",
                                   foreground_color="black",
                                   hint_text="Add an item:",
                                   multiline=False,
                                   size_hint=(1, 0.15),
                                   pos_hint={"x":0.5,"y":0.4}
                                    )
            self.item_field.bind(text=self.item_description.setter("text"))
            self.input_field.add_widget(self.item_description)
            self.input_field.add_widget(self.item_field)
            self.field_counter += 1
        elif self.field_counter == 1:
            self.item_description2 = Label(color="white",
                                          size_hint=(0.5, 0.15),
                                          pos_hint={"x": 0.0, "y": 0.25}
                                          )
            self.item_field2 = TextInput(background_color="white",
                                        foreground_color="black",
                                        hint_text="Add an item:",
                                        multiline=False,
                                        size_hint=(1, 0.15),
                                        pos_hint={"x":0.5,"y":0.25}
                                        )
            self.item_field2.bind(text=self.item_description2.setter("text"))
            self.input_field.add_widget(self.item_description2)
            self.input_field.add_widget(self.item_field2)
            self.field_counter += 1
        else:
            pass


if __name__ == '__main__':
    Christmas().run()
