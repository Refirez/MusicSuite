import customtkinter as ctk


class VideoInfoCard(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.configure(
            corner_radius=12,
            border_width=1
        )

        self.grid_columnconfigure(1, weight=1)

        # --------------------------
        # Thumbnail (placeholder)
        # --------------------------

        self.thumbnail = ctk.CTkLabel(
            self,
            text="🖼",
            width=180,
            height=100,
            corner_radius=8,
            fg_color=("gray80", "gray20"),
            font=("Segoe UI", 40)
        )

        self.thumbnail.grid(
            row=0,
            column=0,
            rowspan=5,
            padx=15,
            pady=15
        )

        # --------------------------

        self.title = ctk.CTkLabel(
            self,
            text="Nenhum vídeo carregado",
            font=("Segoe UI", 18, "bold"),
            anchor="w"
        )

        self.title.grid(
            row=0,
            column=1,
            sticky="w",
            padx=(0, 15),
            pady=(15, 5)
        )

        # --------------------------

        self.channel = ctk.CTkLabel(
            self,
            text="Canal: -",
            anchor="w"
        )

        self.channel.grid(
            row=1,
            column=1,
            sticky="w",
            padx=(0, 15)
        )

        # --------------------------

        self.duration = ctk.CTkLabel(
            self,
            text="Duração: --:--",
            anchor="w"
        )

        self.duration.grid(
            row=2,
            column=1,
            sticky="w",
            padx=(0, 15)
        )

        # --------------------------

        self.views = ctk.CTkLabel(
            self,
            text="Visualizações: -",
            anchor="w"
        )

        self.views.grid(
            row=3,
            column=1,
            sticky="w",
            padx=(0, 15)
        )

        # --------------------------

        self.date = ctk.CTkLabel(
            self,
            text="Publicado em: -",
            anchor="w"
        )

        self.date.grid(
            row=4,
            column=1,
            sticky="w",
            padx=(0, 15),
            pady=(0, 15)
        )

    def update_info(self, video):

        self.title.configure(
            text=video["title"]
        )

        self.channel.configure(
            text=f'Canal: {video["channel"]}'
        )

        self.duration.configure(
            text=f'Duração: {video["duration"]}'
        )

        self.views.configure(
            text=f'Visualizações: {video["views"]}'
        )

        self.date.configure(
            text=f'Publicado em: {video["date"]}'
        )