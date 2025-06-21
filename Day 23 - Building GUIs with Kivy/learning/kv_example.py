# KV Example

from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder

class ButtopnApp(App):
    def build(self):
        return Builder.load_file("button.kv") 
    
    def on_press_button(self):
        print('You pressed button')
        

if __name__ == '__main__':
    app = ButtopnApp()
    app.run()










    