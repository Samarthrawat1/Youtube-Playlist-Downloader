from pytubefix import YouTube, Playlist
import os
import ffmpeg

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


class Merger:
    @staticmethod
    def merge_audio_video(video_path, audio_path, output_path):
        video = ffmpeg.input(video_path)
        audio = ffmpeg.input(audio_path)
        ffmpeg.output(video, audio, output_path).run()
        print(f"Merged video and audio to: {output_path}")

class PlaylistDownloader:
    def __init__(self, playlist_url, path='.', video_resolution='highest', audio_bitrate='highest', merge=True):
        self.playlist = Playlist(playlist_url)
        self.path = path
        self.video_resolution = video_resolution
        self.audio_bitrate = audio_bitrate
        self.merge = merge
    
    def download_playlist(self):
        for video_url in self.playlist.video_urls:
            video_manager = VideoManager(video_url)
            audio_manager = AudioManager(video_url)

            video_path = video_manager.download_video(path=self.path, resolution=self.video_resolution)
            audio_path = audio_manager.download_audio(path=self.path, abr=self.audio_bitrate)

            if self.merge:
                base_name = os.path.splitext(os.path.basename(video_path))[0]
                output_path = os.path.join(self.path, f"{base_name}_merged.mp4")
                Merger.merge_audio_video(video_path, audio_path, output_path)

# Example usage

if __name__ == "__main__":  
    playlist_url = 'YOUR_PLAYLIST_URL'
    path_to_download = 'path_to_download_folder'

    downloader = PlaylistDownloader(playlist_url, path=path_to_download, video_resolution='720p', audio_bitrate='128kbps', merge=True)
    downloader.download_playlist()