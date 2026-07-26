import yt_dlp


class YouTubeManager:

    @staticmethod
    def get_info(url: str):
        ydl_opts = {
            "quiet": True,
            "skip_download": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            return ydl.extract_info(url, download=False)