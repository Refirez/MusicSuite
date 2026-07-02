import customtkinter as ctk

from ui.components.feature_card import FeatureCard


class HomePage(ctk.CTkFrame):

    def __init__(self, master):
        super().__init__(master)

        self.grid_columnconfigure((0,1), weight=1)

        titulo = ctk.CTkLabel(
            self,
            text="Bem-vindo ao MusicSuite",
            font=("Segoe UI", 34, "bold")
        )

        titulo.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(40,10)
        )

        subtitulo = ctk.CTkLabel(
            self,
            text="Escolha uma ferramenta para começar.",
            font=("Segoe UI",18),
            text_color="gray70"
        )

        subtitulo.grid(
            row=1,
            column=0,
            columnspan=2,
            pady=(0,40)
        )

        downloader = FeatureCard(
            self,
            "⬇",
            "Downloader",
            "Baixe músicas em MP3 com thumbnail e metadados."
        )

        splitter = FeatureCard(
            self,
            "✂",
            "Splitter",
            "Separe shows completos em várias músicas."
        )

        biblioteca = FeatureCard(
            self,
            "📁",
            "Biblioteca",
            "Organize todas as músicas baixadas."
        )

        configuracoes = FeatureCard(
            self,
            "⚙",
            "Configurações",
            "Escolha pasta, tema e qualidade."
        )

        downloader.grid(row=2,column=0,padx=25,pady=20)

        splitter.grid(row=2,column=1,padx=25,pady=20)

        biblioteca.grid(row=3,column=0,padx=25,pady=20)

        configuracoes.grid(row=3,column=1,padx=25,pady=20)