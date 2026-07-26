import threading
import customtkinter as ctk
from tkinter import filedialog, messagebox

from services.download_service import DownloadService
from services.youtube_service import YoutubeService


class DownloaderPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.download_folder = ""
        self.service = DownloadService()
        self.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(self, text="Downloader", font=("Segoe UI", 30, "bold")).pack(pady=(30, 6))
        ctk.CTkLabel(self, text="Para conteúdo que você tem autorização para baixar. A capa do vídeo será incorporada ao áudio.", text_color="gray70").pack(pady=(0, 22))
        ctk.CTkLabel(self, text="Link do vídeo", font=("Segoe UI", 15, "bold")).pack(anchor="w", padx=50)
        self.url_entry = ctk.CTkEntry(self, height=40, placeholder_text="https://youtube.com/...")
        self.url_entry.pack(fill="x", padx=50, pady=(5, 18))

        options = ctk.CTkFrame(self, fg_color="transparent")
        options.pack(fill="x", padx=50)
        self.format_var = ctk.StringVar(value="mp3")
        ctk.CTkLabel(options, text="Formato", font=("Segoe UI", 15, "bold")).grid(row=0, column=0, sticky="w")
        ctk.CTkOptionMenu(options, values=["mp3", "flac", "wav"], variable=self.format_var).grid(row=1, column=0, pady=(5, 18), sticky="w")
        ctk.CTkLabel(options, text="Qualidade MP3", font=("Segoe UI", 15, "bold")).grid(row=0, column=1, padx=(35, 0), sticky="w")
        self.quality = ctk.CTkOptionMenu(options, values=["320 kbps", "256 kbps", "192 kbps", "128 kbps"])
        self.quality.set("192 kbps")
        self.quality.grid(row=1, column=1, padx=(35, 0), pady=(5, 18), sticky="w")

        ctk.CTkLabel(self, text="Destino", font=("Segoe UI", 15, "bold")).pack(anchor="w", padx=50)
        row = ctk.CTkFrame(self, fg_color="transparent")
        row.pack(fill="x", padx=50, pady=(5, 22))
        self.folder_label = ctk.CTkLabel(row, text="Nenhuma pasta selecionada", anchor="w")
        self.folder_label.pack(side="left", fill="x", expand=True)
        ctk.CTkButton(row, text="Escolher", width=120, command=self.choose_folder).pack(side="right")

        self.download_button = ctk.CTkButton(self, text="Baixar áudio", height=45, font=("Segoe UI", 16, "bold"), command=self.download)
        self.download_button.pack(fill="x", padx=50, pady=(5, 18))
        self.progress = ctk.CTkProgressBar(self)
        self.progress.pack(fill="x", padx=50)
        self.progress.set(0)
        self.status = ctk.CTkLabel(self, text="Pronto para baixar.")
        self.status.pack(pady=14)

    def choose_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.download_folder = folder
            self.folder_label.configure(text=folder)

    def download(self):
        url = self.url_entry.get().strip()
        if not url or not self.download_folder:
            messagebox.showwarning("Faltam dados", "Informe o link e a pasta de destino.")
            return
        self.download_button.configure(state="disabled")
        self.progress.set(0)
        self.status.configure(text="Preparando download...")
        quality = self.quality.get().split()[0]
        threading.Thread(target=self._download_worker, args=(url, self.format_var.get(), quality), daemon=True).start()

    def _download_worker(self, url, audio_format, quality):
        try:
            self.service.download_audio(url, self.download_folder, audio_format, quality, self._set_progress)
            self.after(0, lambda: self.status.configure(text="Download concluído."))
        except Exception as error:
            message = str(error).replace("\x1b[0;31m", "").replace("\x1b[0m", "")
            if "HTTP Error 403" in message:
                message = (
                    "O YouTube recusou este vídeo (HTTP 403), mesmo após a tentativa "
                    "alternativa. Atualize o yt-dlp e, se persistir, instale um runtime "
                    "JavaScript como Deno."
                )
            self.after(0, lambda: messagebox.showerror("Não foi possível baixar", message))
            self.after(0, lambda: self.status.configure(text="Download não concluído."))
        finally:
            self.after(0, lambda: self.download_button.configure(state="normal"))

    def _set_progress(self, value):
        self.after(0, lambda: (self.progress.set(value), self.status.configure(text=f"Baixando... {value:.0%}")))
