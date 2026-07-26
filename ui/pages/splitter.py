import threading
import customtkinter as ctk
from tkinter import filedialog, messagebox

from core.splitter import parse_chapters, split_audio


class SplitterPage(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.source = ""
        self.destination = ""
        self.grid_columnconfigure(0, weight=1)
        ctk.CTkLabel(self, text="Separar show em faixas", font=("Segoe UI", 30, "bold")).pack(pady=(25, 5))
        ctk.CTkLabel(self, text="Cole os capítulos da descrição ou dos comentários e revise antes de exportar.", text_color="gray70").pack(pady=(0, 18))
        self._file_row("Arquivo de áudio", "source", "Escolher áudio")
        self._file_row("Pasta de saída", "destination", "Escolher pasta")
        ctk.CTkLabel(self, text="Capítulos", font=("Segoe UI", 15, "bold")).pack(anchor="w", padx=50, pady=(15, 4))
        self.chapters_text = ctk.CTkTextbox(self, height=190)
        self.chapters_text.pack(fill="both", expand=True, padx=50)
        self.chapters_text.insert("1.0", "00:00 Abertura\n04:32 Nome da música\n08:15 Próxima música")
        self.format_var = ctk.StringVar(value="mp3")
        ctk.CTkOptionMenu(self, values=["mp3", "wav"], variable=self.format_var, width=110).pack(anchor="w", padx=50, pady=(12, 0))
        self.button = ctk.CTkButton(self, text="Separar faixas", height=45, font=("Segoe UI", 16, "bold"), command=self.start)
        self.button.pack(fill="x", padx=50, pady=12)
        self.progress = ctk.CTkProgressBar(self)
        self.progress.pack(fill="x", padx=50)
        self.progress.set(0)
        self.status = ctk.CTkLabel(self, text="Pronto para separar um arquivo local.")
        self.status.pack(pady=12)

    def _file_row(self, label, attribute, button):
        ctk.CTkLabel(self, text=label, font=("Segoe UI", 15, "bold")).pack(anchor="w", padx=50)
        row = ctk.CTkFrame(self, fg_color="transparent")
        row.pack(fill="x", padx=50, pady=(4, 8))
        value = ctk.CTkLabel(row, text="Não selecionado", anchor="w")
        value.pack(side="left", fill="x", expand=True)
        setattr(self, f"{attribute}_label", value)
        command = self.choose_source if attribute == "source" else self.choose_destination
        ctk.CTkButton(row, text=button, width=140, command=command).pack(side="right")

    def choose_source(self):
        file = filedialog.askopenfilename(filetypes=[("Áudio", "*.mp3 *.m4a *.wav *.flac *.ogg"), ("Todos", "*.*")])
        if file:
            self.source = file
            self.source_label.configure(text=file)

    def choose_destination(self):
        folder = filedialog.askdirectory()
        if folder:
            self.destination = folder
            self.destination_label.configure(text=folder)

    def start(self):
        try:
            chapters = parse_chapters(self.chapters_text.get("1.0", "end"))
            if not self.source or not self.destination:
                raise ValueError("Selecione o áudio e a pasta de saída.")
        except ValueError as error:
            messagebox.showwarning("Revise os dados", str(error))
            return
        self.button.configure(state="disabled")
        self.progress.set(0)
        self.status.configure(text=f"Separando {len(chapters)} faixas...")
        threading.Thread(target=self._split_worker, args=(chapters,), daemon=True).start()

    def _split_worker(self, chapters):
        try:
            files = split_audio(self.source, self.destination, chapters, self.format_var.get(), progress_callback=self._progress)
            self.after(0, lambda: self.status.configure(text=f"Concluído: {len(files)} faixas criadas."))
        except Exception as error:
            self.after(0, lambda: messagebox.showerror("Não foi possível separar", str(error)))
            self.after(0, lambda: self.status.configure(text="Separação não concluída."))
        finally:
            self.after(0, lambda: self.button.configure(state="normal"))

    def _progress(self, value):
        self.after(0, lambda: self.progress.set(value))
