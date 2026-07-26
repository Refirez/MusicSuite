import customtkinter as ctk

from ui.components.sidebar import Sidebar


class MusicSuite(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("🎵 MusicSuite")

        self.geometry("1200x700")
        self.minsize(1000, 650)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar = Sidebar(self)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        self.content = ctk.CTkFrame(self, corner_radius=0)
        self.content.grid(row=0, column=1, sticky="nsew")
        self.pages = {}
        from ui.pages.home import HomePage
        home = HomePage(self.content)

        home.place(
        relx=0,
        rely=0,
        relwidth=1,
        relheight=1
        )

        self.pages["home"] = home