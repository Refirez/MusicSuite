import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class MusicSuite(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("🎵 MusicSuite")
        self.geometry("1000x650")
        self.minsize(900, 600)


if __name__ == "__main__":
    app = MusicSuite()
    app.mainloop()