from commandmanager import CommandParser,Command
from pprint import pprint
import llama
import audio_manager
from file_operations import read_config
import flet as ft
import datetime

base_prompt = f"""
SYSTEM:
Date of today is {datetime.datetime.now().strftime("%d/%m/%Y")}
User's name is {read_config()['username']}
User's email is {read_config()['user_mail']}
You are a text parser AI that simplifies commands relative to these commands given below: 
IF User wants you to set a reminder respond with "I will set a reminder at x time"
IF User wants you to arranga a meeting respond with "I will arrange a meeting at x time"
IF User wants you to send an email respond with "I will send an email to x with content y"
IF User wants you to send a text respond with "I will send a text to x with content y"
IF User wants you to get summary of a paragraph respond with summary of the paragraph
IF User wants you to get summary of a book respond with summary of the book if you dont know the book respond with "I will try to get summary of the book named x from https://fourminutebooks.com/book-summaries/"
IF User wants tou to get summary of a website content respond with "I will try to get summary of the website named x"
IF User says something else respond normally

USER:
Arrange a meeting at 3pm
BOT:
I will arrange a meeting at 15.00 {datetime.datetime.now().strftime("%d/%m/%Y")}, {read_config()['username']}
"""


class ChatterPage(ft.UserControl):
    old_prompts = ""
    commandList = []
    def build(self):
        self.recorder = None
        self.messages = ft.Column(alignment=ft.CrossAxisAlignment.START)
        self.input = ft.TextField(hint_text="Type your message here", expand=True)
        self.record_button = ft.FloatingActionButton(icon=ft.icons.MIC, on_click=self.record_audio)

        view = ft.Column(
            [
                ft.Text("Chat"),
                ft.Row([
                    self.input,
                    ft.FloatingActionButton(icon=ft.icons.SEND, on_click=self.send_message),
                    self.record_button,
                ],
                    vertical_alignment=ft.CrossAxisAlignment.END),
                self.messages,
                
            ],    
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True)
        
        return view
    
    def send_message(self, e=None, message=None):
        if message is None:
            message = self.input.value

        messageToSend = "USER:\n" + message

        if self.messages.controls is None:
            self.messages.controls = []

        self.messages.controls.append(self.message(message=message, is_user=True))
        self.messages.update()
        self.page.update()

        response = llama.generate_response((base_prompt + self.old_prompts + messageToSend + "BOT:"))
        self.old_prompts += messageToSend + "\nBOT:" + response + "\n"
        pprint(self.old_prompts)

        self.messages.controls.append(self.message(message=response, is_user=False))
        self.messages.update()
        self.page.update()
    
    def record_audio(self, e=None):
        if self.recorder is None:
            self.recorder = audio_manager.AudioRecording()
        self.recorder.recording()


        if self.recorder.record.is_set():
            self.record_button.icon = ft.icons.STOP
        else:
            print("stopped")
            self.record_button.icon = ft.icons.MIC
            self.record_button.update()
            self.page.update()

            self.send_message(message=self.recorder.analyze_audio())

        self.record_button.update()
        self.page.update()

    def message(self, message, is_user=True):
        if is_user:
            return ft.Container(
                content=ft.Text(message),
                border_radius=10,
                bgcolor="#3F3F3F",
                alignment=ft.alignment.top_left,

            )
        else:
            content_to_return = ft.Row([])

            if message.startswith("I will") or message.startswith("\nI will") or message.startswith("\n\nI will"):
                self.set_command(message)
                content_to_return.controls.append(ft.ElevatedButton(text="Confirm",on_click=self.apply_command))

            content_to_return.controls.append(ft.Text(message, color="#000000"))

            return ft.Container(
                        content=content_to_return,
                        border_radius=10,
                        bgcolor="#F0F0F0",
                        alignment=ft.alignment.top_left,
                    )
    def set_command(self, command):
        self.commandList.append(CommandParser().parse(command))

        print("command set")           

    def apply_command(self = None, e=None) :
        commandId = len(self.commandList) - 1

        print(self.commandList[commandId])

        if commandId is not None:
            command = Command(
                command=self.commandList[commandId]["command"],
                time=self.commandList[commandId]["time"],
                to=self.commandList[commandId]["to"],
                content=self.commandList[commandId]["content"],
                named=self.commandList[commandId]["named"],
                )
            command.apply_command()
        else:
            print("commandId is None")

        print("command applied")

        

def main(page: ft.Page):
    page.title = "Chat"
    page.theme_mode = ft.ThemeMode.DARK

    messaging = ChatterPage()

    page.add(messaging)
    page.update()



if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER,port = 5000)

