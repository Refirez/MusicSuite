import yt_dlp

from core.utils import format_date, format_views, seconds_to_time


class YouTubeManager:

    @staticmethod
    def get_info(url: str):
        ydl_opts = {
            "quiet": True,
            "skip_download": True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)

        return {
            "title": info.get("title", "Sem título"),
            "channel": info.get("channel") or info.get("uploader", "-"),
            "duration": seconds_to_time(info.get("duration")),
            "views": format_views(info.get("view_count")),
            "date": format_date(info.get("upload_date")),
            "thumbnail": info.get("thumbnail"),
            "description": info.get("description", ""),
        }
