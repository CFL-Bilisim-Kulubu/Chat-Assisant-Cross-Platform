
import llama
import audio_manager
#import file_operations
import flet as ft


class ChatterPage(ft.UserControl):
    def build(self):
        self.recorder = None
        self.messages = ft.Column()
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

        if self.messages.controls is None:
            self.messages.controls = []

        self.messages.controls.append(self.message(message=message, is_user=True))
        self.messages.controls.append(self.message(message=llama.generate_response(message), is_user=False))
        self.messages.update()
        self.page.update()
        print(message)
    
    def record_audio(self, e=None):
        if self.recorder is None:
            self.recorder = audio_manager.AudioRecording()
        self.recorder.recording()


        if self.recorder.record.is_set():
            self.record_button.icon = ft.icons.STOP
        else:
            print("stopped")
            self.record_button.icon = ft.icons.MIC
            self.send_message(message=self.recorder.analyze_audio())

        self.record_button.update()
        self.page.update()

    def message(self, message, is_user=True):
        if is_user:
            return ft.Container(
                content=ft.Text(message),
                border_radius=10,
            )
        else:
            return ft.Container(
                        content=ft.Text(message, color="#000000"),
                        border_radius=10,
                        bgcolor="#F1F0F0",
                    )
    
        

def main(page: ft.Page):
    page.title = "Chat"
    page.theme_mode = ft.ThemeMode.DARK

    messaging = ChatterPage()

    page.add(messaging)
    page.update()



if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER,port = 5000)

