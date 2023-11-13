from tkinter import *
from Settings.colors import *
from Settings.images import *
from Presentacion.ICitas import ICitas

class IMenu:
    
    def __init__(self):
        #window configuration
        self.window = Tk()
        self.window.title("ApaCreator")
        self.window.geometry("400x400")
        self.window.resizable(False, False)
        #definimos una imagen para ponerla como icono de la aplicacion
        icon = PhotoImage(file=imgIcon)
        self.window.config(bg=color_bg)
        self.window.iconphoto(False, icon)
        self.title = Label(self.window, text="ApaCreator", bg=color_bg, fg=color_fg, font=("Garamond", 30))
        self.title.pack(pady=20)
        
        #button configuration
        #los botones centrados al margen izquierdo
        #definimos las imagenes para los botones
        kitty1 = PhotoImage(file=imgButton1)
        kitty2 = PhotoImage(file=imgButton2)
        
        self.citasButton = Button(self.window, text=" Generar Citas", bg=color_bg_button, fg=color_fg_button, width=300, height=70, font=("Garamond", 15), activebackground=color_bg_button, activeforeground=color_fg_button, image=kitty1, compound='left')
        self.citasButton.pack(pady=20)
        self.resetButton = Button(self.window, text=" Resetear Datos", bg=color_bg_button, fg=color_fg_button, width=300, height=70, font=("Garamond", 15), activebackground=color_bg_button, activeforeground=color_fg_button, image=kitty2, compound='left')
        self.resetButton.pack(pady=20)
        
        self.window.mainloop()
        