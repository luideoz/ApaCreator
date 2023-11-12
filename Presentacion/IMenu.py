from tkinter import *
from Settings.colors import *

class IMenu:
    
    def __init__(self):
        #window configuration
        self.window = Tk()
        self.window.title("ApaCreator")
        self.window.geometry("450x450")
        self.window.resizable(False, False)
        #definimos una imagen para ponerla como icono de la aplicacion
        icon = PhotoImage(file="media/libro-magico.png")
        self.window.config(bg=color_bg)
        self.window.iconphoto(False, icon)
        self.title = Label(self.window, text="ApaCreator", bg=color_bg, fg=color_fg, font=("Garamond", 30))
        self.title.pack(pady=20)
        
        #button configuration
        #los botones centrados al margen izquierdo
        self.citasButton = Button(self.window, text=" Generar Citas", bg=color_bg_button, fg=color_fg_button, width=50, height=2, font=("Garamond", 15), activebackground=color_bg_button, activeforeground=color_fg_button)
        self.citasButton.pack(pady=5)
        self.autoresButtton = Button(self.window, text= "Ver autores", bg=color_bg_button, fg=color_fg_button, width=50, height=2, font=("Garamond", 15), activebackground=color_bg_button, activeforeground=color_fg_button)
        self.autoresButtton.pack(pady=5)
        self.editorialButton = Button(self.window, text="Ver editoriales", bg=color_bg_button, fg=color_fg_button, width=50, height=2, font=("Garamond", 15), activebackground=color_bg_button, activeforeground=color_fg_button)
        self.editorialButton.pack(pady=5)
        self.articulosButton = Button(self.window, text="Ver articulos", bg=color_bg_button, fg=color_fg_button, width=50, height=2, font=("Garamond", 15), activebackground=color_bg_button, activeforeground=color_fg_button)
        self.articulosButton.pack(pady=5)
        
        self.window.mainloop()
        