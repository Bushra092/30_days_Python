from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        #add widgets to window

        self.window.add_widget(Image(source = 'Image.jfif'))
        self.gretting = Label(text = 'What is your name')
        self.window.add_widget(self.gretting)
        self.user = TextInput(multiline = False)
        self.window.add_widget(self.user)

        self.button = Button(text = 'Greet')
        self.button.bind(on_press = self.callback)
        self.window.add_widget(self.button)
        
        return self.window

    def callback(self, instance):
        self.gretting.text ='Hello '+ self.user.text +' !'


    

if __name__ == "__main__":
    SayHello().run()