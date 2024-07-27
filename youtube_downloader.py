import os
import ffmpeg
from pytubefix import YouTube, Playlist

class VideoManager:
    def __init__(self, video_url):
        try:
            self.video = YouTube(video_url)
        except Exception as e:
            print(f"Failed to initialize YouTube object for {video_url}: {e}")
    
    def list_resolutions(self):
        return [stream.resolution for stream in self.video.streams.filter(type='video')]

    def download_video(self, path='.', resolution='highest'):
        if resolution == 'highest':
            stream = self.video.streams.get_highest_resolution()
        else:
            stream = self.video.streams.filter(resolution=resolution, type='video').first()
        video_path = stream.download(output_path=path)
        print(f"Downloaded video: {self.video.title}")
        return video_path

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
        try:
            self.video = YouTube(video_url)
        except Exception as e:
            print(f"Failed to initialize YouTube object for {video_url}: {e}")
    
    def list_audio_formats(self):
        return [stream.abr for stream in self.video.streams.filter(only_audio=True)]

    def download_audio(self, path='.', abr='highest'):
        if abr == 'highest':
            stream = self.video.streams.filter(only_audio=True).order_by('abr').desc().first()
        else:
            stream = self.video.streams.filter(abr=abr, only_audio=True).first()
        audio_path = stream.download(output_path=path)
        print(f"Downloaded audio: {self.video.title}")
        return audio_path

    def get_audio_info(self):
        info = {
            'title': self.video.title,
            'length': self.video.length,
            'views': self.video.views,
            'author': self.video.author
        }
        return info

class Merger:
    @staticmethod
    def merge_audio_video(video_path, audio_path, output_path):
        if os.path.exists(video_path) and os.path.exists(audio_path):
            video = ffmpeg.input(video_path)
            audio = ffmpeg.input(audio_path)
            ffmpeg.output(video, audio, output_path).run()
            print(f"Merged video and audio to: {output_path}")
        else:
            print(f"Cannot merge files. Video or audio file does not exist: {video_path}, {audio_path}")

class PlaylistDownloader:
    def __init__(self, playlist_url, path='.', merge=True):
        self.playlist = Playlist(playlist_url)
        self.path = path
        self.merge = merge
    
    def get_user_choice(self, options, option_type):
        print(f"Available {option_type}:")
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        choice = int(input(f"Select {option_type} by number: ")) - 1
        return options[choice]

    def download_playlist(self, max_resolution=False):
        for video_url in self.playlist.video_urls:
            video_manager = VideoManager(video_url)
            audio_manager = AudioManager(video_url)
            if max_resolution:
                selected_resolution = 'highest'
                selected_bitrate = 'highest'
            if not max_resolution:
            # List and get user choice for video resolution
                resolutions = video_manager.list_resolutions()
                selected_resolution = self.get_user_choice(resolutions, 'resolution')

                # List and get user choice for audio bitrate
                bitrates = audio_manager.list_audio_formats()
                selected_bitrate = self.get_user_choice(bitrates, 'bitrate')
            
            video_path = video_manager.download_video(path=self.path, resolution=selected_resolution)
            audio_path = audio_manager.download_audio(path=self.path, abr=selected_bitrate)

            if self.merge:
                base_name = os.path.splitext(os.path.basename(video_path))[0]
                output_path = os.path.join(self.path, f"{base_name}_merged.mp4")
                Merger.merge_audio_video(video_path, audio_path, output_path)
