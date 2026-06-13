import customtkinter as ctk


class MainScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = ctk.CTkLabel(self, text="YouTube Downloader", font=("Arial", 20))
        self.label.pack(pady=30)
        self.video_btn = ctk.CTkButton(
            self, text="Download Video", command=self.open_video
        )
        self.video_btn.pack(pady=10)
        self.audio_btn = ctk.CTkButton(
            self, text="Download Audio", command=self.open_audio
        )
        self.audio_btn.pack(pady=10)

    def open_video(self):
        self.master.master.show_video()

    def open_audio(self):
        self.master.master.show_audio()
