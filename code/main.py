from pprint import pprint
import llama
import audio_manager
from file_operations import read_config
import flet as ft
import datetime
from desktop_notifier import DesktopNotifier

notifier = DesktopNotifier()

base_prompt = f"""
SYSTEM:
You are a helpful assistant

Now answer to the user

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
    
    async def send_message(self, e=None, message=None):
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
        
        await notifier.send(title="Cross Platform Chat Assisant", message="Response completed!")
    
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
            content_to_return.controls.append(ft.Text(message, color="#000000"))

            return ft.Container(
                        content=content_to_return,
                        border_radius=10,
                        bgcolor="#F0F0F0",
                        alignment=ft.alignment.top_left,
                    )
         

    

        

def main(page: ft.Page):
    page.title = "Chat"
    page.theme_mode = ft.ThemeMode.DARK

    messaging = ChatterPage()

    page.add(messaging)
    page.update()



if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER,port = 5000)

