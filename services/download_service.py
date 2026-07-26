from core.downloader_engine import Downloader


class DownloadService:
    """Small boundary between the interface and yt-dlp."""

    def __init__(self):
        self.downloader = Downloader()

    def download_audio(self, url, folder, audio_format, quality, progress_callback=None):
        self.downloader.download_audio(
            url, folder, audio_format, quality, progress_callback
        )
