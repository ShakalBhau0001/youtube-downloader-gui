# 📥 YouTube Downloader GUI

### YouTube Audio & Video Downloader — Modern CustomTkinter GUI powered by yt-dlp

**YouTube Downloader GUI** is a clean, modern, and beginner-friendly desktop application built entirely in **Python (3.12.x compatible)**.

It provides an intuitive graphical interface for downloading YouTube videos and audio without requiring terminal commands or browser extensions.

Using a simple sidebar-based interface, users can:

* 🎬 Download YouTube videos in selectable quality presets (144p–1080p)
* 🎵 Extract audio as MP3 with selectable bitrates (128 kbps, 192 kbps, and 320 kbps)
* ℹ️ View detailed video information before downloading
* ⚡ Perform downloads in the background without freezing the interface
* 📂 Automatically manage download directories and file naming

All operations run **fully locally** — no accounts, no tracking, and no background services.

---

## 🖥️ Looking for the CLI Version?

If you prefer terminal workflows and command-line automation:

👉 **CLI Repository:** https://github.com/ShakalBhau0001/youtube-downloader-cli

---

## ✨ Key Philosophy

YouTube Downloader GUI follows three core principles:

### 1️⃣ Simplicity First

A clean and minimal interface focused on getting downloads done quickly.

### 2️⃣ Beginner Friendly

No command memorization or technical setup beyond installation.

### 3️⃣ Modular Architecture

Downloader logic and GUI components are separated for maintainability and future expansion.

---

## ✨ Features

* 🎬 Download YouTube videos in multiple quality presets
* 🎵 Extract audio as MP3 with selectable bitrates
* ℹ️ Fetch and view video information before downloading
* 🖥️ Modern desktop interface built with CustomTkinter
* ⚡ Background downloading using Python threading
* 📂 Automatic output directory management
* ✅ URL validation and error handling
* 🔒 Fully local operation with no external services

---

## 🎬 Video Downloader

Download YouTube videos in your preferred quality.

### Supported Presets

* 144p
* 240p
* 360p
* 480p
* 720p
* 1080p

### Features

* Best available video selection
* Quality selector
* Automatic file naming
* Background downloading
* Success and error notifications

### Use Cases

> Lecture downloads, offline viewing, content archival, educational resources

---

## 🎵 Audio Downloader

Download only the audio track from YouTube videos.

### Supported Bitrates

* 128 kbps
* 192 kbps
* 320 kbps

### Features

* MP3 extraction
* Bitrate selector
* Automatic file naming
* Background downloading
* Success and error notifications

### Use Cases

> Music listening, podcasts, lecture audio, and offline playlists

---

## ℹ️ Video Information Viewer

Preview information about a video before downloading.

### Displays

* Video Title
* Channel Name
* Duration
* View Count
* Upload Date
* Description

### Use Cases

> Verify content before downloading and inspect video metadata.

---

## 🖥️ User Interface

The application uses a sidebar-driven navigation system built with CustomTkinter.

### Screens

* Main Screen
* Video Downloader
* Audio Downloader
* Video Information Viewer
* About Page

### Features

* Modern dark-themed interface
* Responsive layout
* Simple navigation
* Beginner-friendly design

---

## 📁 Project Structure

```bash
youtube-downloader-gui/
│
├── assets/
│   ├── Audio.png
│   ├── Video.png
│   ├── D-Audio.png
│   ├── D-Video.png
│   └── Info.png
│
├── core/
│   ├── __init__.py
│   └── downloader.py
│
├── gui/
│   ├── __init__.py
│   ├── app.py
│   │
│   ├── screens/
│   │   ├── __init__.py
│   │   ├── about_screen.py
│   │   ├── audio_screen.py
│   │   ├── info_screen.py
│   │   ├── main_screen.py
│   │   └── video_screen.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
│
├── main.py
├── requirements.txt
├── LICENSE
└── README.md
```

> ✔ Core downloading logic and GUI components are strictly separated for maintainability and extensibility.

---

## 🧪 Tech Stack

| Component         | Implementation   |
| ----------------- | ---------------- |
| Downloader Engine | yt-dlp           |
| GUI Framework     | CustomTkinter    |
| Media Processing  | FFmpeg           |
| Threading         | Python threading |
| Interface Toolkit | Tkinter          |
| Language          | Python 3.12.x    |

---

## 🚀 Getting Started

### 1️⃣ Clone Repository

```bash
git clone https://github.com/ShakalBhau0001/youtube-downloader-gui.git
cd youtube-downloader-gui
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt**

```txt
customtkinter
yt-dlp
```

---

### 3️⃣ Install FFmpeg

FFmpeg is required for:

* MP3 audio extraction
* Audio conversion and post-processing
* Bitrate selection support

Without FFmpeg, video downloads will work normally, but audio downloads and MP3 conversion may fail.

---

#### Windows

1. Download FFmpeg from:

https://ffmpeg.org/download.html

2. Extract the downloaded archive.

3. Locate the `bin` folder.

4. Add the `bin` folder to your system `PATH`.

5. Verify installation:

```bash
ffmpeg -version
```

---

#### Linux

```bash
sudo apt install ffmpeg
```

---

#### macOS

```bash
brew install ffmpeg
```

---

### Verify Installation

```bash
ffmpeg -version
```

If FFmpeg is installed correctly, version information will be displayed.

---

### 4️⃣ Launch Application

```bash
python main.py
```

---

## ⚠️ Important Notes

* Supports valid YouTube URLs only
* Downloads run in background threads
* Files are automatically named using the video title
* Download directories are created automatically if they do not exist
* Internet connection is required
* FFmpeg is required for MP3 extraction and audio conversion

---

## 🛣️ Roadmap

* Playlist download support
* Thumbnail preview
* Download progress bars
* Custom directory picker
* Download history
* PyInstaller standalone executable
* Linux and macOS packaging

---

## ⚠️ Disclaimer

This project is intended for **personal, educational, and research use only**.

Downloading copyrighted content without permission may violate YouTube's Terms of Service.

The developer is **not responsible** for misuse of this application.

Always respect content creators and platform policies.

---

## 🪪 Author

**Developer:** Shakalen Shaikh

**GitHub:** https://github.com/ShakalBhau0001

---

> *"Great software hides complexity behind simplicity."*

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

---
