"""
This is a small project which is about a chatbot. Basically this chat bot learns the answer to a question from the user.
This type of bot is usefull for applications that uses customised chatbot.
Owners can use API like chatGPT but it is found that you still can get answers to irrelevant questions,
for example, in a project for finding the best house, you dont want the bot to solve integration.

There will be multiple models and each models will have a different fuctions.

Creator: Ruhan Saad Dave
"""

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen, ScreenManager, CardTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from gui_style import *
from simple_bot import *

class ChatBotPage(Screen):
    def __init__(self, **kwargs):
        super(ChatBotPage, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation = "vertical")
        top = BoxLayout(size_hint_y = 0.2)
        tool_btn = Button(text = "Tools", size_hint_x = 0.2, on_press = self.tool)
        label = LBLabel(text = "Chat Bot")
        top.add_widget(tool_btn)
        top.add_widget(label)
        self.layout.add_widget(top)

        mid = BoxLayout(orientation = "vertical")
        self.scroll = ScrollView(do_scroll_y = True)
        self.grid = GridLayout(cols = 1, size_hint_y = None)
        self.grid.bind(minimum_height = self.grid.setter('height'))
        
        user = "Chat Bot:"
        answer = "Hi, Im your friendly chatbot. How can I help you?"
        btn_layout = BoxLayout(size_hint_y = None, height = 100)
        user_type = RLabel(text = f"{user}", size_hint_x = 0.2)
        user_text = ChatTextInput(text = f"{answer}", font_size = 20)
        btn_layout.add_widget(user_type)
        btn_layout.add_widget(user_text)
        self.grid.add_widget(btn_layout)

        self.scroll.add_widget(self.grid)
        mid.add_widget(self.scroll)
        self.layout.add_widget(mid)

        bottom = BoxLayout(size_hint_y = 0.2)
        self.textinput = MyTextInput(hint_text = "Enter something?")
        send_btn = Button(text = "Send", size_hint_x = 0.2, on_press = self.send)
        bottom.add_widget(self.textinput)
        bottom.add_widget(send_btn)
        self.layout.add_widget(bottom)

        self.add_widget(self.layout)
        
    def tool(self, instance):
        self.manager.transition = CardTransition(direction = "right", mode = "push")
        self.manager.current = "toolpage"

    def send(self,instance):
        btn_layout = BoxLayout(size_hint_y = None, height = 100)
        btn_img = LBLabel(text = f"You:", size_hint_x = 0.2)
        btn_layout.add_widget(btn_img)
        user_text = ChatMyTextInput(text = f"{self.textinput.text}", font_size = 20)
        response = ask_chatbot(self.textinput.text)
        self.textinput.text = ""
        btn_layout.add_widget(user_text)
        self.grid.add_widget(btn_layout)
        
        #Function that asks chatbot for reply and display on screen
        btn_layout = BoxLayout(size_hint_y = None, height = 100)
        btn_img = RLabel(text = f"Chat Bot:", size_hint_x = 0.2)
        btn_layout.add_widget(btn_img)
        self.bot_text = ChatTextInput(text = "Thinking of a suitable reply...", font_size = 20)
        btn_layout.add_widget(self.bot_text)
        self.grid.add_widget(btn_layout)
        self.bot_text.text = f"{response}"

class ToolPage(Screen):
    def __init__(self, **kwargs):
        super(ToolPage, self).__init__(**kwargs)
        layout = BoxLayout(orientation = "vertical")

        top = BoxLayout(size_hint_y = 0.2)
        back_btn = Button(text = "Back", size_hint_x = 0.2, on_press = self.back)
        label = Label(text = "Tools")
        top.add_widget(back_btn)
        top.add_widget(label)
        layout.add_widget(top)

        self.add_widget(layout)
    
    def back(self, instance):
        self.manager.transition = CardTransition(direction = "left",  mode = "pop")
        self.manager.current = "chatbotpage"



class ChatBotApp(App):
    def build(self):
        screen_manager = ScreenManager()
        screen_manager.add_widget(ChatBotPage(name = "chatbotpage"))
        screen_manager.add_widget(ToolPage(name = "toolpage"))
        
        return screen_manager
    
if __name__ == "__main__":
    ChatBotApp().run()


    
