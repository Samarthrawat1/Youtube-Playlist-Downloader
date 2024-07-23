import pytubefix


class download_playlist:
    def __init__(self, playlist_url, download_path):
        self.playlist_url = playlist_url
        self.download_path = download_path
    
    def list_videos(self):
        playlist = pytubefix.Playlist(self.playlist_url)
        self.playlist = playlist
        return playlist.video_urls
    
    def list_resolutions(self):
        resolutions = []
        for video in self.playlist.videos:
            stream = video.streams.get_highest_resolution()
            resolutions.append(stream.resolution)
        return resolutions