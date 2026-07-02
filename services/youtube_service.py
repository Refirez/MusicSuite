from yt_dlp import YoutubeDL


class YouTubeService:

    @staticmethod
    def get_info(url: str):

        options = {

            "quiet": True,

            "skip_download": True,

            "extract_flat": False,

            "noplaylist": True

        }

        with YoutubeDL(options) as ydl:

            info = ydl.extract_info(url, download=False)

            return {

                "title": info.get("title"),

                "channel": info.get("uploader"),

                "duration": info.get("duration"),

                "thumbnail": info.get("thumbnail"),

                "views": info.get("view_count"),

                "upload_date": info.get("upload_date")

            }