from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.storage.jsonstore import JsonStore
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.label import Label
from datetime import date

x = date.today().year


class wish_overview(Screen, RelativeLayout):
    #Widget Layouts:
    def __init__(self, **kwargs):
        super(wish_overview, self).__init__(**kwargs)
        self.title_overview = Label(text=f"Wish lists {str(date.today().year)}", size_hint=(0.4, 0.1), pos_hint={"x": 0.3, "y": 0.80}, font_size=20)
        self.change_window = Button(text="Change to Wishes", size_hint=(0.2, 0.1), pos_hint={"x": 0.65, "y": 0.0})
        self.add_wishlist = Button(text="Add (No Function)", size_hint=(0.2, 0.1), pos_hint={"x": 0.35, "y": 0.0})

    #Widget adding
        self.add_widget(self.title_overview)
        self.change_window.bind(on_press=self.change_to_wishes)
        self.add_widget(self.change_window)
        self.add_widget(self.add_wishlist)

    def change_to_wishes(self, *args):
        self.manager.current="wish_screen"

class wish_screen(Screen, RelativeLayout):

    def __init__(self, **kwargs):
        super(wish_screen, self).__init__(**kwargs)
        self.wish_y_axis = 0.6 # variable to move wishes downwards
        self.check_wish_y_axis = 0.576  # variable to move checkboxes downwards
        self.wish_counter = 1  # variable for amount of wishes
        self.wish_counter_range = 1
        self.upper_border = 0

        self.store = JsonStore('Data_CB_advent2024.json')

        #Widget-Layouts
        self.text_name = TextInput(background_color="white",
                                   foreground_color="black",
                                   hint_text="Please enter your Name:",
                                   multiline=False,
                                   text=self.data_loader_name(),
                                   size_hint=(0.4, 0.1),
                                   pos_hint={"x": 0.3, "y": 0.9}
                                   )
        self.text_age = TextInput(background_color="white",
                                  foreground_color="black",
                                  hint_text="Please enter your Age:",
                                  multiline=False,
                                  text=self.data_loader_age(),
                                  size_hint=(0.4, 0.05),
                                  pos_hint={"x": 0.3, "y": 0.85}
                                  )
        self.text_adress = TextInput(background_color="white",
                                     foreground_color="black",
                                     hint_text="Please enter your Adress:",
                                     multiline=False,
                                     text=self.data_loader_adress(),
                                     size_hint=(0.4, 0.15),
                                     pos_hint={"x": 0.3, "y": 0.7}
                                     )
        self.button_wish_add = Button(text="Add a wish", size_hint=(0.1, 0.1), pos_hint={"x": 0.15, "y": 0.0})
        self.button_wish_remove = Button(text="Remove previous wish", size_hint=(0.2, 0.1), pos_hint={"x": 0.65, "y": 0.0})
        self.change_window = Button(text="Change to Wish-Overview", size_hint=(0.25, 0.1), pos_hint={"x": 0.35, "y": 0.0})

        # Validation-Fields for name, age and adress-fields:
        self.text_name.bind(on_text_validate=self.name_validation)
        self.text_age.bind(on_text_validate=self.age_validation)
        self.text_adress.bind(on_text_validate=self.adress_validation)

        # Data-Storage for name, age and adress
        self.text_name.bind(on_text_validate=self.data_storage)
        self.text_age.bind(on_text_validate=self.data_storage)
        self.text_adress.bind(on_text_validate=self.data_storage)

        #Data-Storage for wishes:


        # Adding the Widget-Fields:
        self.add_widget(self.text_name)
        self.add_widget(self.text_age)
        self.add_widget(self.text_adress)
        self.button_wish_add.bind(on_press=self.add_wish)
        self.add_widget(self.button_wish_add)
        self.button_wish_remove.bind(on_press=self.delete_wish)
        self.add_widget(self.button_wish_remove)
        self.change_window.bind(on_press=self.change_to_wishes)
        self.add_widget(self.change_window)

    # Functions validation of name, age and adress:
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

    # Function to save data after quitting the app and load them after restarting the app for namen, age and adress
    def data_storage(self, *args):
        self.store.put("person_data", name=self.text_name.text, age=self.text_age.text,
                           adress=self.text_adress.text)
    def data_loader_name(self, *args):
        try:
            return self.store.get("person_data")["name"]
        except KeyError:
            return ""

    def data_loader_age(self, *args):
        try:
            return self.store.get("person_data")["age"]
        except KeyError:
            return ""

    def data_loader_adress(self, *args):
        try:
            return self.store.get("person_data")["adress"]
        except KeyError:
            return ""

#Functions for wish- and checkbox-widgets:
    def add_wish(self, *args):
        if self.wish_counter < 11:
            for i in range(0, self.wish_counter, self.wish_counter_range):
                self.item_field = TextInput(background_color="red",
                                        foreground_color="black",
                                        hint_text="Add a wish:",
                                        multiline=False,
                                        pos_hint={"x": 0.4, "y": self.wish_y_axis},
                                        size_hint=(0.2, 0.05))
                self.wish_status = CheckBox(size_hint=(0.1, 0.1), pos_hint={"x": 0.3, "y": self.check_wish_y_axis})
                self.wish_status.bind(active=self.finished_wish)
                #self.item_field.bind(on_text_validate=self.wish_data1)
                self.add_widget(self.item_field)
                self.add_widget(self.wish_status)
                self.check_wish_y_axis -= 0.05
                self.upper_border += 2
                self.wish_counter += 1
                self.wish_counter_range += 1
                self.wish_y_axis -= 0.05
        else:
            pass

    def finished_wish(self, *args):
        for i in range(0, self.upper_border, 2):
            if self.children[i].active:
                self.children[i+1].background_color = "green"
            else:
                self.children[i+1].background_color = "red"


    #Function to delete wishes
    def delete_wish(self, *args):
        if self.wish_counter > 1:
            self.remove_widget(self.children[0])
            self.remove_widget(self.children[0])
            self.check_wish_y_axis += 0.05
            self.wish_counter -= 1
            self.wish_y_axis += 0.05
            self.wish_counter_range -= 1
            self.upper_border -= 2
        else:
            pass

    # Function to change the Screen
    def change_to_wishes(self, *args):
        self.manager.current="wish_overview"


class Christmas(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(wish_overview(name="wish_overview"))
        sm.add_widget(wish_screen(name="wish_screen"))
        return sm

if __name__ == '__main__':
    Christmas().run()
