import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(
            master,
            width=220,
            corner_radius=0
        )

        self.pack_propagate(False)

        titulo = ctk.CTkLabel(
            self,
            text="🎵 MusicSuite",
            font=("Segoe UI", 24, "bold")
        )

        titulo.pack(pady=(30, 40))

        botoes = [
            "🏠 Home",
            "⬇ Downloader",
            "✂ Splitter",
            "📁 Biblioteca",
            "⚙ Configurações"
        ]

        for texto in botoes:

            botao = ctk.CTkButton(
                self,
                text=texto,
                width=180,
                height=42,
                anchor="w",
                corner_radius=10
            )

            botao.pack(pady=6)