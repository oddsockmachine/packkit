import kivy
kivy.require('1.0.9')
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import NumericProperty
from kivy.app import App

Builder.load_string('''
<HelloWorldScreen>:

    cols: 2
    Button:
        text: "Button 1"
    Button:
        text: "Button 2"
        font_size: 24
    Button:
        text: "Button 3"
        background_color: .7, .7, 1, 1
    Button:
        text: "Button 4"
        on_press: self.text = 'pressed'
        on_release: self.text = 'Button 4'
    ToggleButton:
        text: "A toggle button"
    ToggleButton:
        text: "a toggle button in a group"
        group: "money"
    ToggleButton:
        text: "A toggle in the down state"
        state: "down"
    ToggleButton:
        text: "another toggle button in a group"
        group: "money"

''')

class HelloWorldScreen(GridLayout):
    counter = NumericProperty(0)
    def my_callback(self):
        print 'The button has been pushed'
        self.counter += 1

class HelloWorldApp(App):
    def build(self):
        return HelloWorldScreen()

if __name__ == '__main__':
    HelloWorldApp().run()