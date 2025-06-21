

#! 🎯 Challenge
#? - Convert the temperature converter CLI tool into a GUI tool


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label

class TempConverterApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        self.input_temp = TextInput(hint_text="Enter temperature", multiline=False, padding=10)
        self.result_label = Label(text="")
        
        buttonLayout = BoxLayout(orientation='horizontal', padding=10, spacing=10)
        btn_ctof = Button(text="Convert to °F")
        btn_ctof.bind(on_press=self.convert_to_fahrenheit)

        btn_ftoc = Button(text="Convert to °C")
        btn_ftoc.bind(on_press=self.convert_to_celsius)

        layout.add_widget(self.input_temp)
        buttonLayout.add_widget(btn_ctof)
        buttonLayout.add_widget(btn_ftoc)
        layout.add_widget(buttonLayout)
        layout.add_widget(self.result_label)

        return layout

    def convert_to_fahrenheit(self, instance):
        try:
            celsius = float(self.input_temp.text)
            fahrenheit = (celsius * 9/5) + 32
            self.result_label.text = f"{celsius}°C = {fahrenheit:.2f}°F"
        except ValueError:
            self.result_label.text = "Invalid input! Enter a number."

    def convert_to_celsius(self, instance):
        try:
            fahrenheit = float(self.input_temp.text)
            celsius = (fahrenheit - 32) * 5/9
            self.result_label.text = f"{fahrenheit}°F = {celsius:.2f}°C"
        except ValueError:
            self.result_label.text = "Invalid input! Enter a number."

if __name__ == '__main__':
    TempConverterApp().run()
