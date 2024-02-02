from tkinter import Tk, PhotoImage, Label, Entry, Button, StringVar, W, E, N, S, Listbox, Frame
from tkinter import ttk, messagebox
import logging
import os

class IMain:
    def __init__(self):
        self.config = self.load_config()
        if not os.path.isdir("Logs"):
            os.mkdir("Logs")

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler("Logs/IMain.log")
        handler.setLevel(logging.ERROR)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        logging.info("Logger inicializado correctamente")
        self.window = Tk()
        self.window.title("Generador de Citas APA")
        icon = None
        try:
            icon = PhotoImage(file=self.config["icon-image"])
            logging.info("Icono cargado correctamente")
        except Exception as e:
            self.window.withdraw()
            messagebox.showerror("Error", "No se pudo cargar el icono de la aplicacion. Por favor, asegurese de que el archivo existe y esta en la carpeta media y que este especificado en el archivo settings.config")
            logging.error("Error al cargar el icono de la aplicacion")
            """paramos la ejecucion del programa"""
            return
        self.window.iconphoto(False, icon)
        self.window.resizable(False, False)
        self.window.geometry("1000x600")
        logging.info("Dimensiones de la ventana inicializadas correctamente")
        try:
            self.window.configure(background=self.config["background-color"])
            logging.info("Color de fondo cargado correctamente")
        except Exception as e:
            self.window.withdraw()
            messagebox.showerror("Error", "No se pudo cargar el color de fondo de la aplicacion. Por favor, asegurese de que el color esta especificado en el archivo settings.config")
            logging.error("Error al cargar el color de fondo de la aplicacion")
            return
        """creamos las diversas pestañas"""
        self.tab_control = ttk.Notebook(self.window)
        self.tab_autores = ttk.Frame(self.tab_control)
        self.tab_editorial = ttk.Frame(self.tab_control)
        self.tab_articulos = ttk.Frame(self.tab_control)
        self.tab_citas = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_autores, text="Autores")
        self.tab_control.add(self.tab_editorial, text="Editorial")
        self.tab_control.add(self.tab_articulos, text="Articulos")
        self.tab_control.add(self.tab_citas, text="Citas")
        self.tab_control.place(x=0, y=0, width=1000, height=600)
        logging.info("Pestañas creadas correctamente")
        logging.info("Ventana inicializada correctamente")

        """FRAME DE AUTORES"""
        self.frame_autores = Frame(self.tab_autores, background=self.config["background-color"])
        self.frame_autores.place(x=0, y=0, width=1000, height=600)
        self.list_autores = Listbox(self.frame_autores, background=self.config["listbox-background-color"], font=(self.config["font-family"], self.config["font-size"]), width=30, height=25)
        self.list_autores.place(x=10, y=10)
        self.lbl_nombre = Label(self.frame_autores, text="Nombre", background=self.config["background-color"], font=(self.config["font-family"], self.config["lbl-font-size"]), foreground=self.config["foreground"])
        self.lbl_nombre.place(x=600, y=10)
        self.entry_nombre = Entry(self.frame_autores, font=(self.config["font-family"], self.config["entry-font-size"]), width=30)
        self.entry_nombre.place(x=450, y=45)
        self.lbl_apellido1 = Label(self.frame_autores, text="Apellido 1", background=self.config["background-color"], font=(self.config["font-family"], self.config["lbl-font-size"]), foreground=self.config["foreground"])
        self.lbl_apellido1.place(x=600, y=100)
        self.entry_apellido1 = Entry(self.frame_autores, font=(self.config["font-family"], self.config["entry-font-size"]), width=30)
        self.entry_apellido1.place(x=450, y=135)
        self.lbl_apellido2 = Label(self.frame_autores, text="Apellido 2", background=self.config["background-color"], font=(self.config["font-family"], self.config["lbl-font-size"]), foreground=self.config["foreground"])
        self.lbl_apellido2.place(x=600, y=190)
        self.entry_apellido2 = Entry(self.frame_autores, font=(self.config["font-family"], self.config["entry-font-size"]), width=30)
        self.entry_apellido2.place(x=450, y=225)
        self.btn_agregar_autor = Button(self.frame_autores, text="Agregar", font=(self.config["font-family"], self.config["btn-font-size"]), width=self.config["btn-size"])
        self.btn_agregar_autor.place(x=500, y=300)
        self.btn_eliminar_autor = Button(self.frame_autores, text="Eliminar", font=(self.config["font-family"], self.config["btn-font-size"]), width=self.config["btn-size"])
        self.btn_eliminar_autor.place(x=500, y=350)
        self.btn_reset_autor = Button(self.frame_autores, text="Reset", font=(self.config["font-family"], self.config["btn-font-size"]), width=self.config["btn-size"])
        self.btn_reset_autor.place(x=500, y=400)
        self.btn_back = Button(self.frame_autores, text="Volver", font=(self.config["font-family"], self.config["btn-font-size"]), width=15)
        self.btn_back.place(x=350, y=500)
        self.btn_next = Button(self.frame_autores, text="Siguiente", font=(self.config["font-family"], self.config["btn-font-size"]), width=15)
        self.btn_next.place(x=730, y=500)

        self.window.mainloop()

    
    def load_config(self):
        config = {}
        with open("Settings/settings.config" ,"r") as f:
            for line in f:
                line = line.replace("\n","")
                line = line.split(":")
                line[1].replace(" ","")
                config[line[0]] = line[1][:len(line[1])-1]
        return config