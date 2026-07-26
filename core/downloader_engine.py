from yt_dlp import YoutubeDL
from yt_dlp.utils import DownloadError
from pathlib import Path
import shutil


class Downloader:

    def __init__(self):
        pass

    def download_audio(
        self,
        url,
        folder,
        audio_format="mp3",
        quality="192",
        progress_callback=None
    ):
        Path(folder).mkdir(parents=True, exist_ok=True)
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": str(Path(folder) / "%(title)s.%(ext)s"),
            "noplaylist": True,
            "windowsfilenames": True,
            "quiet": True,
            "noprogress": True,
            "no_color": True,
            "retries": 3,
            # A thumbnail do vídeo é incorporada como capa do arquivo final.
            "writethumbnail": audio_format != "wav",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": audio_format,
                "preferredquality": quality,
            }, {
                "key": "EmbedThumbnail",
                "already_have_thumbnail": False,
            }] if audio_format != "wav" else [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": audio_format,
                "preferredquality": quality,
            }],
            "progress_hooks": [
                lambda d: self.progress_hook(
                    d,
                    progress_callback
                )
            ]
        }

        # O yt-dlp só habilita Deno por padrão. Habilitamos o Node.js local
        # para resolver os desafios JavaScript exigidos pelo YouTube.
        node_path = shutil.which("node")
        if node_path:
            ydl_opts["js_runtimes"] = {"node": {"path": node_path}}
            # Scripts oficiais do yt-dlp usados para os desafios JavaScript do
            # YouTube; evita formatos ausentes por "n challenge".
            ydl_opts["remote_components"] = ["ejs:github"]

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
        except DownloadError as error:
            # Alguns vídeos recusam as URLs do cliente padrão com HTTP 403.
            # O web_safari disponibiliza formatos HLS que não dependem do
            # desafio JavaScript em muitos desses casos.
            if "HTTP Error 403" not in str(error):
                raise
            fallback_opts = {
                **ydl_opts,
                "extractor_args": {"youtube": {"player_client": ["web_safari"]}},
            }
            with YoutubeDL(fallback_opts) as ydl:
                ydl.download([url])

    def progress_hook(
        self,
        data,
        callback
    ):

        if callback is None:
            return

        if data.get("status") == "downloading":

            total = data.get("total_bytes")

            downloaded = data.get("downloaded_bytes", 0)

            if total:

                percent = downloaded / total

                callback(percent)

        elif data.get("status") == "finished":

            callback(1.0)
