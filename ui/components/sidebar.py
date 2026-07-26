import customtkinter as ctk


class Sidebar(ctk.CTkFrame):

    def __init__(self, master, navigate_callback):
        super().__init__(
            master,
            width=220,
            corner_radius=0
        )

        self.pack_propagate(False)

        self.navigate_callback = navigate_callback

        titulo = ctk.CTkLabel(
            self,
            text="🎵 MusicSuite",
            font=("Segoe UI", 24, "bold")
        )

        titulo.pack(pady=(30, 40))

        self.buttons = {}

        menu_items = [
            ("🏠 Home", "home"),
            ("⬇ Downloader", "downloader"),
            ("✂ Splitter", "splitter"),
            ("📁 Biblioteca", "library"),
            ("⚙ Configurações", "settings")
        ]

        for text, page in menu_items:

            button = ctk.CTkButton(
                self,
                text=text,
                width=180,
                height=42,
                anchor="w",
                corner_radius=10,
                command=lambda p=page: self.navigate(p)
            )

            button.pack(pady=6)

            self.buttons[page] = button

    def navigate(self, page):

        self.navigate_callback(page)