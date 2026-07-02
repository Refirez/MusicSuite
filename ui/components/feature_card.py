import customtkinter as ctk


class FeatureCard(ctk.CTkFrame):

    def __init__(self, master, icon, title, description, command=None):
        super().__init__(
            master,
            width=280,
            height=180,
            corner_radius=18,
            fg_color="#303030"
        )

        self.pack_propagate(False)

        self.command = command

        self.bind("<Button-1>", self.click)

        self.icon = ctk.CTkLabel(
            self,
            text=icon,
            font=("Segoe UI Emoji", 38)
        )
        self.icon.pack(pady=(18, 6))

        self.title = ctk.CTkLabel(
            self,
            text=title,
            font=("Segoe UI", 22, "bold")
        )
        self.title.pack()

        self.description = ctk.CTkLabel(
            self,
            text=description,
            text_color="gray70",
            wraplength=220,
            justify="center",
            font=("Segoe UI", 14)
        )
        self.description.pack(pady=(8, 18))

        for widget in (self.icon, self.title, self.description):
            widget.bind("<Button-1>", self.click)

        self.bind("<Enter>", self.hover_enter)
        self.bind("<Leave>", self.hover_leave)

        for widget in (self.icon, self.title, self.description):
            widget.bind("<Enter>", self.hover_enter)
            widget.bind("<Leave>", self.hover_leave)

    def hover_enter(self, event):
        self.configure(fg_color="#3B3B3B")

    def hover_leave(self, event):
        self.configure(fg_color="#303030")

    def click(self, event):
        if self.command:
            self.command()