from core.youtube_client import YouTubeManager


class YoutubeService:

    def __init__(self):
        self.youtube = YouTubeManager()

    def get_video_info(self, url: str):
        return self.youtube.get_info(url)
