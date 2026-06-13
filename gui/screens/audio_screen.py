import customtkinter as ctk
import threading
from tkinter import messagebox
from core.downloader import download_audio, get_download_path
from gui.utils.helpers import is_valid_url


class AudioScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        ctk.CTkLabel(self, text="Download Audio", font=("Arial", 18)).pack(pady=20)
        self.url_entry = ctk.CTkEntry(
            self, width=400, placeholder_text="Enter YouTube URL"
        )
        self.url_entry.pack(pady=10)
        self.bitrate = ctk.CTkOptionMenu(self, values=["128", "192", "320"])
        self.bitrate.set("192")
        self.bitrate.pack(pady=5)
        ctk.CTkButton(self, text="Download", command=self.start_download).pack(pady=10)

    def start_download(self):
        url = self.url_entry.get()

        if not is_valid_url(url):
            messagebox.showerror("Error", "Invalid YouTube URL")
            return

        bitrate = self.bitrate.get()
        threading.Thread(target=self.download, args=(url, bitrate), daemon=True).start()

    def download(self, url, bitrate):
        try:
            download_audio(url=url, output_dir=get_download_path(), bitrate=bitrate)
            messagebox.showinfo("Success", "Audio Downloaded ✅")
        except Exception as e:
            messagebox.showerror("Error", str(e))
