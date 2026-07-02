import customtkinter as ctk

from ui.widgets.video_info_card import VideoInfoCard

ctk.set_appearance_mode("dark")

app = ctk.CTk()

app.geometry("700x300")

card = VideoInfoCard(app)

card.pack(fill="both", expand=True, padx=20, pady=20)

card.update_info({

    "title": "ALEE SHOW - PLANTÃO FESTIVAL",

    "channel": "beatriz",

    "duration": "57:01",

    "views": "7.5 mil",

    "date": "04/05/2026"

})

app.mainloop()