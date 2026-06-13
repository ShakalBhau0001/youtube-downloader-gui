import customtkinter as ctk


class AboutScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        ctk.CTkLabel(self, text="About", font=("Arial", 20)).pack(pady=20)
        ctk.CTkLabel(
            self,
            text="YouTube Downloader\n\nDownload Video & Audio easily.\n\nBuilt with Python ",
            justify="center",
        ).pack(pady=10)
        ctk.CTkLabel(
            self,
            text="Developer: Shakalen Shaikh \n Follow For More :- github.com/ShakalBhau0001 \n Version: 1.0",
        ).pack(pady=20)
