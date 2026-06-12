import customtkinter as ctk
from gui.screens.video_screen import VideoScreen
from gui.screens.audio_screen import AudioScreen
from gui.screens.info_screen import InfoScreen
from gui.screens.about_screen import AboutScreen


class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Downloader")
        self.geometry("800x450")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.sidebar = ctk.CTkFrame(self, width=150)
        self.sidebar.grid(row=0, column=0, sticky="ns")
        ctk.CTkButton(self.sidebar, text="Video", command=self.show_video).pack(pady=20)
        ctk.CTkButton(self.sidebar, text="Audio", command=self.show_audio).pack(pady=20)
        ctk.CTkButton(self.sidebar, text="Info", command=self.show_info).pack(pady=20)
        ctk.CTkButton(self.sidebar, text="About", command=self.show_about).pack(pady=20)
        self.container = ctk.CTkFrame(self)
        self.container.grid(row=0, column=1, sticky="nsew")
        self.current_screen = None
        self.show_video()

    def clear_screen(self):
        if self.current_screen:
            self.current_screen.destroy()

    def show_video(self):
        self.clear_screen()
        self.current_screen = VideoScreen(self.container)
        self.current_screen.pack(fill="both", expand=True)

    def show_audio(self):
        self.clear_screen()
        self.current_screen = AudioScreen(self.container)
        self.current_screen.pack(fill="both", expand=True)

    def show_about(self):
        self.clear_screen()
        self.current_screen = AboutScreen(self.container)
        self.current_screen.pack(fill="both", expand=True)

    def show_info(self):
        self.clear_screen()
        self.current_screen = InfoScreen(self.container)
        self.current_screen.pack(fill="both", expand=True)
