# gui_app.py

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from youtube_downloader import PlaylistDownloader

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Playlist Downloader")

        # Playlist URL input
        self.url_label = ttk.Label(root, text="Playlist URL:")
        self.url_label.grid(column=0, row=0, padx=10, pady=10)
        self.url_entry = ttk.Entry(root, width=50)
        self.url_entry.grid(column=1, row=0, padx=10, pady=10)

        # Download Path selection
        self.path_label = ttk.Label(root, text="Download Path:")
        self.path_label.grid(column=0, row=1, padx=10, pady=10)
        self.path_entry = ttk.Entry(root, width=50)
        self.path_entry.grid(column=1, row=1, padx=10, pady=10)
        self.path_button = ttk.Button(root, text="Browse", command=self.browse_path)
        self.path_button.grid(column=2, row=1, padx=10, pady=10)

        # Merge Option
        self.merge_var = tk.BooleanVar(value=True)
        self.merge_check = ttk.Checkbutton(root, text="Merge Video and Audio", variable=self.merge_var)
        self.merge_check.grid(column=0, row=2, padx=10, pady=10)

        # Download Highest quality
        self.highest_quality_var = tk.BooleanVar(value=True)
        self.highest_quality_check = ttk.Checkbutton(root, text="Dwnload highest quality", variable=self.highest_quality_var)
        self.highest_quality_check.grid(column=2, row=2, padx=10, pady=10)

        # Download Button
        self.download_button = ttk.Button(root, text="Download Playlist", command=self.download_playlist)
        self.download_button.grid(column=1, row=3, padx=10, pady=10)

    def browse_path(self):
        path = filedialog.askdirectory()
        if path:
            self.path_entry.delete(0, tk.END)
            self.path_entry.insert(0, path)

    def download_playlist(self):
        playlist_url = self.url_entry.get()
        download_path = self.path_entry.get()
        merge = self.merge_var.get()
        highest_quality = self.highest_quality_var.get()

        if not playlist_url or not download_path:
            messagebox.showerror("Error", "Please provide both playlist URL and download path.")
            return

        try:
            downloader = PlaylistDownloader(playlist_url, path=download_path, merge=merge)
            downloader.download_playlist(max_resolution = highest_quality)
            messagebox.showinfo("Success", "Playlist downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to download playlist: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
