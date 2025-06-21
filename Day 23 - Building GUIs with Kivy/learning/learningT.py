

from kivy.app import App
from kivy.uix.label import Label #?HELLO FROM KIVY 
from kivy.uix.image import Image #?Display image
from kivy.uix.button import Button #? Multiple buttons
from kivy.uix.boxlayout import BoxLayout
import random 



red = [1,0,0,1]
green = [0,1,0,1]
blue = [0,0,1,1]
purple = [1,0,1,1]

colors = [red, green, blue, purple]

class HBoxLayoutExample(App):
    def build(self):
        layout = BoxLayout(padding = 10)

        for i in range(5):
            btn = Button(text = f'Button #{i+1}', background_color = random.choice(colors)
                         )
            btn.index = i+1
            btn.bind(on_press = self.on_press_button)

            layout.add_widget(btn)

        return layout  

    def on_press_button(self, instance):
        print(f"You presses Button #{instance.index}")  



# class MainApp(App):
#     def build(self):
#         # label = Label(text = 'Hello From Kivy',  font_size = '40sp')

#         # image = Image(source = 'Image.jfif')
#         return image

if __name__ == '__main__':
    # app = MainApp()
    app = HBoxLayoutExample()
    app.run()
