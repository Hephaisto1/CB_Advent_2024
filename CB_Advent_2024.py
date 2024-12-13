from kivy.app import App
from kivy.uix.stacklayout import StackLayout
from kivy.uix.textinput import TextInput
from kivy.storage.dictstore import DictStore
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.relativelayout import RelativeLayout
class Christmas(App):

    def build(self):
        self.check_wish_y_axis = 0.576
        self.wish_counter = 0
        self.store = DictStore('Data_CB_advent2024.py')
        self.interface = RelativeLayout()
        self.input_field = RelativeLayout()
        self.wish = StackLayout(orientation="lr-tb", pos_hint={"x":0.4,"y":0.6}, size_hint=(0.2,0.05))
        if len(self.store.keys()) == 0:
            self.text_name = TextInput(background_color="white",
                                       foreground_color="black",
                                       hint_text="Please enter your Name:",
                                       multiline=False,
                                       size_hint=(0.4,0.1),
                                       pos_hint={"x":0.3,"y":0.90})
            self.text_age = TextInput(background_color="white",
                                      foreground_color="black",
                                      hint_text="Please enter your Age:",
                                      multiline=False,
                                      size_hint=(0.4, 0.05),
                                      pos_hint={"x":0.3,"y":0.85}
                                      )
            self.text_adress = TextInput(background_color="white",
                                         foreground_color="black",
                                         hint_text="Please enter your Adress:",
                                         multiline=False,
                                         size_hint=(0.4, 0.15),
                                         pos_hint={"x":0.3,"y":0.7}
                                         )
        else:
            self.text_name = TextInput(background_color="white",
                                       foreground_color="black",
                                       hint_text="Please enter your Name:",
                                       multiline=False,
                                       text=self.store.get("person_data")["name"],
                                       size_hint=(0.4, 0.1),
                                       pos_hint={"x":0.3,"y":0.9}
                                       )
            self.text_age = TextInput(background_color="white",
                                      foreground_color="black",
                                      hint_text="Please enter your Age:",
                                      multiline=False,
                                      text=self.store.get("person_data")["age"],
                                      size_hint=(0.4, 0.05),
                                      pos_hint={"x":0.3,"y":0.85}
                                      )
            self.text_adress = TextInput(background_color="white",
                                         foreground_color="black",
                                         hint_text="Please enter your Adress:",
                                         multiline=False,
                                         text=self.store.get("person_data")["adress"],
                                         size_hint=(0.4, 0.15),
                                         pos_hint={"x":0.3,"y":0.7}
                                         )
        self.button_add = Button(text="Add",size_hint=(0.1, 0.1),pos_hint={"x":0.45,"y":0.0})
        self.text_name.bind(on_text_validate=self.name_validation)
        self.text_age.bind(on_text_validate=self.age_validation)
        self.text_adress.bind(on_text_validate=self.adress_validation)
        self.text_name.bind(on_text_validate=self.data_storage)
        self.text_age.bind(on_text_validate=self.data_storage)
        self.text_adress.bind(on_text_validate=self.data_storage)
        self.input_field.add_widget(self.text_name)
        self.input_field.add_widget(self.text_age)
        self.input_field.add_widget(self.text_adress)
        self.button_add.bind(on_press=self.add_wish)
        self.input_field.add_widget(self.button_add)
        self.interface.add_widget(self.input_field)
        self.interface.add_widget(self.wish)
        return self.interface

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

    def add_wish(self, *args):
        if self.wish_counter < 10:
            self.item_field = TextInput(background_color="white",
                                   foreground_color="black",
                                   hint_text="Add a wish:",
                                   multiline=False)
            self.wish.add_widget(self.item_field)
            self.wish_status = CheckBox(size_hint=(0.1, 0.1), pos_hint={"x": 0.3, "y":self.check_wish_y_axis})
            self.wish_status.bind(active=self.finished_wish)
            self.input_field.add_widget(self.wish_status)
            self.wish_counter += 1
            self.check_wish_y_axis -=0.05

    def finished_wish(self, *args):
        if self.wish_status.active:
            self.item_field.background_color = "green"
        else:
            self.item_field.background_color = "red"

if __name__ == '__main__':
    Christmas().run()

"""
Überlegung: Aktuell können nur zwei Wünsche aufgerufen werden. Überlegen wie die Widgets bzw. das Fenster skaliert werden soll, um mehr Wünsche zu realisieren.
"""