from pytubefix import YouTube, Playlist

class VideoManager:
    def __init__(self, video_url):
        self.video = YouTube(video_url)
    
    def list_resolutions(self):
        return [stream.resolution for stream in self.video.streams.filter(type='video')]

    def download_video(self, path='.', resolution='highest'):
        if resolution == 'highest':
            stream = self.video.streams.get_highest_resolution()
        else:
            stream = self.video.streams.filter(resolution=resolution, type='video').first()
        stream.download(output_path=path)
        print(f"Downloaded: {self.video.title}")

    def get_video_info(self):
        info = {
            'title': self.video.title,
            'length': self.video.length,
            'views': self.video.views,
            'author': self.video.author
        }
        return info
    
class AudioManager:
    def __init__(self, video_url):
        self.video = YouTube(video_url)
    
    def list_audio_formats(self):
        return [stream.abr for stream in self.video.streams.filter(only_audio=True)]

    def download_audio(self, path='.', abr='highest'):
        if abr == 'highest':
            stream = self.video.streams.filter(only_audio=True).order_by('abr').desc().first()
        else:
            stream = self.video.streams.filter(abr=abr, only_audio=True).first()
        stream.download(output_path=path)
        print(f"Downloaded: {self.video.title}")

    def get_audio_info(self):
        info = {
            'title': self.video.title,
            'length': self.video.length,
            'views': self.video.views,
            'author': self.video.author
        }
        return info

class PlaylistManager:
    def __init__(self, playlist_url):
        self.playlist = Playlist(playlist_url)
        self.videos = [VideoManager(video_url) for video_url in self.playlist.video_urls]
    
    def download_all_videos(self, path='.'):
        for video in self.videos:
            video.download_video(path)

    def get_playlist_info(self):
        info = {
            'title': self.playlist.title,
            'length': len(self.playlist.video_urls)
        }
        return info

# Example usage
playlist_url = 'YOUR_PLAYLIST_URL'
playlist_manager = PlaylistManager(playlist_url)

# Download all videos in the playlist
playlist_manager.download_all_videos(path='path_to_download_folder')

# Get playlist info
print(playlist_manager.get_playlist_info())
