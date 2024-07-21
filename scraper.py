from pytube import Playlist
from tqdm import tqdm
import os

def download_youtube_playlist(playlist_url, download_path):
    # Create a Playlist object
    playlist = Playlist(playlist_url)
    
    # Ensure the download path exists
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    # Download each video in the playlist
    for video in tqdm(playlist.videos, desc="Downloading videos", unit="video"):
        try:
            print(f"Downloading: {video.title}")
            stream = video.streams.get_highest_resolution()
            stream.download(output_path=download_path)
            print(f"Downloaded: {video.title}")
        except Exception as e:
            print(f"Failed to download {video.title}: {str(e)}")

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    download_path = input("Enter the download path: ")
    download_youtube_playlist(playlist_url, download_path)
