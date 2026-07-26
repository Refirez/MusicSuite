import os
import sys

# FFmpeg e os componentes JavaScript do yt-dlp escrevem UTF-8. No Windows,
# iniciar o Python em modo UTF-8 evita falhas de decodificação CP-1252 após a
# conversão do áudio.
if sys.platform == "win32" and not sys.flags.utf8_mode:
    os.execv(sys.executable, [sys.executable, "-X", "utf8", *sys.argv])

import customtkinter as ctk

from ui.main_window import MusicSuite

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = MusicSuite()
app.mainloop()
