import tkinter as tk
from tkinter import ttk


class FlatButton(ttk.Label):
    def __init__(self, master: tk.Misc | None,
                 cursor="hand2", padding=(10, 5, 10, 5), command=None, **kwargs):
        if "style" in kwargs.keys():
            self.style = kwargs["style"]
        else:
            self.style = "flatbutton.TLabel"

        ttk.Style().configure("flatbutton.TLabel", background="#1d2024")
        ttk.Style().configure("flatbuttonactive.TLabel", background="#34373b")

        ttk.Label.__init__(self, master, style="flatbutton.TLabel" , cursor=cursor, padding=padding, **kwargs)
        self.bind("<Button-1>", lambda t=None: self._execute(command) if t is not None else None)


    def change_command(self, command):
        self.unbind("<Button-1>")
        self.bind("<Button-1>", lambda t=None: self._execute(command) if t is not None else None)

    def _execute(self, command):
        self._sim_button()
        if command:
            command()

    def _sim_button(self):
        self.configure(style="flatbuttonactive.TLabel")
        self.after(125, func=lambda: self.configure(style=self.style))
