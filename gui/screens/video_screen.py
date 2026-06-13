import customtkinter as ctk
import threading
from tkinter import messagebox
from core.downloader import download_video, get_download_path
from gui.utils.helpers import is_valid_url


class VideoScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        ctk.CTkLabel(self, text="Download Video", font=("Arial", 18)).pack(pady=20)
        self.url_entry = ctk.CTkEntry(
            self, width=400, placeholder_text="Enter YouTube URL"
        )
        self.url_entry.pack(pady=10)
        self.quality = ctk.CTkOptionMenu(
            self, values=["144p", "240p", "360p", "480p", "720p", "1080p"]
        )
        self.quality.set("480p")
        self.quality.pack(pady=5)
        ctk.CTkButton(self, text="Download", command=self.start_download).pack(pady=10)

    def start_download(self):
        url = self.url_entry.get()

        if not is_valid_url(url):
            messagebox.showerror("Error", "Invalid YouTube URL")
            return

        quality = self.quality.get()
        threading.Thread(target=self.download, args=(url, quality), daemon=True).start()

    def download(self, url, quality):
        try:
            download_video(url=url, output_dir=get_download_path(), quality=quality)
            messagebox.showinfo("Success", "Video Downloaded ✅")
        except Exception as e:
            messagebox.showerror("Error", str(e))
