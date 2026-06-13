import customtkinter as ctk
import threading
from tkinter import messagebox
from core.downloader import fetch_info, format_duration, format_views
from gui.utils.helpers import is_valid_url


class InfoScreen(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        ctk.CTkLabel(self, text="Video Info", font=("Arial", 18)).pack(pady=20)
        self.url_entry = ctk.CTkEntry(
            self, width=400, placeholder_text="Enter YouTube URL"
        )
        self.url_entry.pack(pady=10)
        ctk.CTkButton(self, text="Fetch Info", command=self.start_fetch).pack(pady=10)
        self.result = ctk.CTkTextbox(self, width=500, height=200)
        self.result.pack(pady=10)

    def start_fetch(self):
        url = self.url_entry.get()

        if not is_valid_url(url):
            messagebox.showerror("Error", "Invalid YouTube URL")
            return

        threading.Thread(target=self.fetch, args=(url,)).start()

    def fetch(self, url):
        self.result.delete("1.0", "end")

        try:
            info = fetch_info(url)
            text = f"""
                Title: {info['title']}
                Uploader: {info['uploader']}
                Duration: {format_duration(info['duration'])}
                Views: {format_views(info['view_count'])}
                Upload Date: {info['upload_date']}
                Description:
                {info['description']}
            """

            self.result.insert("end", text)

        except Exception as e:
            self.result.insert("end", f"Error: {str(e)}")
