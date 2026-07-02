import customtkinter as ctk

from ui.components.sidebar import Sidebar
from ui.pages.home import HomePage
from ui.pages.downloader import DownloaderPage


class MusicSuite(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.title("🎵 MusicSuite")
        self.geometry("1200x700")
        self.minsize(1000, 650)

        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Sidebar
        self.sidebar = Sidebar(self, self.show_page)
        self.sidebar.grid(row=0, column=0, sticky="ns")

        # Área principal
        self.content = ctk.CTkFrame(self, corner_radius=0)
        self.content.grid(row=0, column=1, sticky="nsew")

        self.pages = {}

        self.pages["home"] = HomePage(self.content)
        self.pages["downloader"] = DownloaderPage(self.content)

        for page in self.pages.values():
            page.place(
                relx=0,
                rely=0,
                relwidth=1,
                relheight=1
            )

        self.show_page("home")

    def show_page(self, page_name):
        page = self.pages.get(page_name)

        if page:
            page.lift()