import tkinter as tk

class HoverButton(tk.Button):
    
    def __init__(self, master, coluna, linha, **kw,):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)
        self.grid(column=coluna, row=linha, padx=10, pady=50, sticky='ew')

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground