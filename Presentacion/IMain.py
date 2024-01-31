from tkinter import Tk, PhotoImage, Label, Entry, Button, StringVar, W, E, N, S
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
        try:
            icon = PhotoImage(file=self.config["icon-image"])
            logging.info("Icono cargado correctamente")
        except Exception as e:
            self.window.withdraw()
            messagebox.showerror("Error", "No se pudo cargar el icono de la aplicacion. Por favor, asegurese de que el archivo existe y esta en la carpeta media y que este especificado en el archivo settings.config")
            logging.error("Error al cargar el icono de la aplicacion",e)
            """paramos la ejecucion del programa"""
            return
        self.window.iconphoto(False, icon)
        self.window.resizable(False, False)
        self.window.geometry("1000x600")
        try:
            self.window.configure(background=self.config["background-color"])
            logging.info("Color de fondo cargado correctamente")
        except Exception as e:
            self.window.withdraw()
            messagebox.showerror("Error", "No se pudo cargar el color de fondo de la aplicacion. Por favor, asegurese de que el color esta especificado en el archivo settings.config")
            logging.error("Error al cargar el color de fondo de la aplicacion",e)
            return



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