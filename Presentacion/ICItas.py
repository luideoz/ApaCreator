from tkinter import *
from Settings.colors import *

class ICitas:
    def __init__(self):
        
        #window configuration
        self.window = Tk()
        self.window.title("Generacion de citas")
        self.window.geometry("750x750")
        self.window.resizable(False, False)
        self.window.config(bg=color_bg)
        
        #empezamos con la parte de eleccion de autor
        #diposicion de la ventana: dividida en dos, en la izquierda tendremos la parte de seleccion de autor si esta creado y en la derecha tendremos la parte de creacion de autor. arriba en el centro texto explicativo y abajo ederecha dos botones:avanzar y retroceder
        #parte izquierda
        self.leftFrame = Frame(self.window, bg="white")
        self.leftFrame.pack(side=LEFT, padx=20, pady=20)
        #parte derecha
        self.rightFrame = Frame(self.window, bg="white")
        self.rightFrame.pack(side=RIGHT, padx=20, pady=20)
        
        
        self.window.mainloop()