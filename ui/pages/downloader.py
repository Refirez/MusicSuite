import customtkinter as ctk
from tkinter import filedialog


class DownloaderPage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.download_folder = ""

        self.grid_columnconfigure(0, weight=1)

        # ------------------------
        # Título
        # ------------------------

        title = ctk.CTkLabel(
            self,
            text="🎵 Downloader",
            font=("Segoe UI", 30, "bold")
        )

        title.pack(pady=(30, 10))

        subtitle = ctk.CTkLabel(
            self,
            text="Baixe músicas do YouTube com thumbnail e metadados",
            font=("Segoe UI", 16)
        )

        subtitle.pack(pady=(0, 30))

        # ------------------------
        # Link
        # ------------------------

        ctk.CTkLabel(
            self,
            text="Link do YouTube",
            font=("Segoe UI", 15, "bold")
        ).pack(anchor="w", padx=50)

        self.url_entry = ctk.CTkEntry(
            self,
            height=40,
            placeholder_text="https://youtube.com/..."
        )

        self.url_entry.pack(fill="x", padx=50, pady=(5, 25))

        # ------------------------
        # Formato
        # ------------------------

        ctk.CTkLabel(
            self,
            text="Formato",
            font=("Segoe UI", 15, "bold")
        ).pack(anchor="w", padx=50)

        self.format_var = ctk.StringVar(value="mp3")

        formats = ctk.CTkFrame(self, fg_color="transparent")
        formats.pack(anchor="w", padx=50, pady=(5, 25))

        for fmt in ["mp3", "flac", "wav"]:
            ctk.CTkRadioButton(
                formats,
                text=fmt.upper(),
                variable=self.format_var,
                value=fmt
            ).pack(side="left", padx=15)

        # ------------------------
        # Qualidade
        # ------------------------

        ctk.CTkLabel(
            self,
            text="Qualidade",
            font=("Segoe UI", 15, "bold")
        ).pack(anchor="w", padx=50)

        self.quality = ctk.CTkOptionMenu(
            self,
            values=[
                "320 kbps",
                "256 kbps",
                "192 kbps",
                "128 kbps"
            ]
        )

        self.quality.pack(anchor="w", padx=50, pady=(5, 25))

        # ------------------------
        # Pasta
        # ------------------------

        ctk.CTkLabel(
            self,
            text="Destino",
            font=("Segoe UI", 15, "bold")
        ).pack(anchor="w", padx=50)

        folder_frame = ctk.CTkFrame(self, fg_color="transparent")
        folder_frame.pack(fill="x", padx=50)

        self.folder_label = ctk.CTkLabel(
            folder_frame,
            text="Nenhuma pasta selecionada",
            anchor="w"
        )

        self.folder_label.pack(side="left", fill="x", expand=True)

        choose_button = ctk.CTkButton(
            folder_frame,
            text="Escolher",
            width=120,
            command=self.choose_folder
        )

        choose_button.pack(side="right")

        # ------------------------
        # Botão
        # ------------------------

        self.download_button = ctk.CTkButton(
            self,
            text="⬇ Baixar",
            height=45,
            font=("Segoe UI", 16, "bold"),
            command=self.download
        )

        self.download_button.pack(fill="x", padx=50, pady=35)

        # ------------------------
        # Barra
        # ------------------------

        self.progress = ctk.CTkProgressBar(self)

        self.progress.pack(fill="x", padx=50)

        self.progress.set(0)

        # ------------------------
        # Status
        # ------------------------

        self.status = ctk.CTkLabel(
            self,
            text="Pronto para baixar."
        )

        self.status.pack(pady=20)

    def choose_folder(self):

        folder = filedialog.askdirectory()

        if folder:

            self.download_folder = folder
            self.folder_label.configure(text=folder)

    def download(self):

        self.status.configure(
            text="(Interface pronta. Download será implementado na próxima etapa.)"
        )