from tkinter import Tk, PhotoImage, Label, Entry, Button, StringVar, W, E, N, S, Listbox, Frame
from tkinter import ttk, messagebox
from Dominio.Autor import Autor
from Dominio.Editorial import Editorial
from Dominio.Articulo import Articulo
import logging
import os

class IMain:
    def __init__(self):
        self.config = self.load_config()
        self.autor_cita = []
        self.editorial_cita = None
        self.articulo_cita = None
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
        self.list_autores = Listbox(self.frame_autores,selectmode='multiple', background=self.config["listbox-background-color"], font=(self.config["font-family"], self.config["font-size"]), width=30, height=25)
        self.list_autores.place(x=10, y=10)
        self.list_autores.bind("<<ListboxSelect>>", lambda x: self.click_list_autores())
        autores = Autor("","","").SelectAurotes()
        for autor in autores:
            self.list_autores.insert("end", autor[1]+" "+autor[2]+" "+autor[0])
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
        self.btn_agregar_autor = Button(self.frame_autores, text="Agregar", font=(self.config["font-family"],  self.config["btn-font-size"]),width=self.config["btn-size"],command=self.agregar_autor)
        self.btn_agregar_autor.place(x=500, y=300)
        self.btn_eliminar_autor = Button(self.frame_autores, text="Eliminar", state="disabled",font=(self.config["font-family"], self.config["btn-font-size"]), width=self.config["btn-size"], command=self.eliminar_autor)
        self.btn_eliminar_autor.place(x=500, y=350)
        self.btn_reset_autor = Button(self.frame_autores, text="Reset", font=(self.config["font-family"], self.config["btn-font-size"]), width=self.config["btn-size"], command=self.reset_autores)
        self.btn_reset_autor.place(x=500, y=400)
        self.btn_back = Button(self.frame_autores, text="Volver", font=(self.config["font-family"], self.config["btn-font-size"]), width=15, state="disabled")
        self.btn_back.place(x=350, y=500)
        self.btn_next = Button(self.frame_autores, text="Siguiente", font=(self.config["font-family"], self.config["btn-font-size"]), width=15, state="disabled", command=self.next_tab_autores)
        self.btn_next.place(x=730, y=500)

        """FRAME DE EDITORIAL"""
        self.frame_editorial = Frame(self.tab_editorial, background=self.config["background-color"])
        self.frame_editorial.place(x=0, y=0, width=1000, height=600)
        self.list_editorial = Listbox(self.frame_editorial, background=self.config["listbox-background-color"], font=(self.config["font-family"], self.config["font-size"]), width=30, height=25)
        self.list_editorial.place(x=10, y=10)
        editoriales = Editorial("").SelectEditoriales()
        for editorial in editoriales:
            self.list_editorial.insert("end", editorial[0])
        self.list_editorial.bind("<<ListboxSelect>>", lambda x: self.click_list_editorial())
        self.lbl_editorial_nombre = Label(self.frame_editorial, text="Nombre", background=self.config["background-color"], font=(self.config["font-family"], self.config["lbl-font-size"]), foreground=self.config["foreground"])
        self.lbl_editorial_nombre.place(x=600, y=10)
        self.entry_editorial_nombre = Entry(self.frame_editorial, font=(self.config["font-family"], self.config["entry-font-size"]), width=30)
        self.entry_editorial_nombre.place(x=450, y=45)
        self.btn_agregar_editorial = Button(self.frame_editorial, text="Agregar", font=(self.config["font-family"], self.config["btn-font-size"]), width=self.config["btn-size"], command=self.agregar_editorial)
        self.btn_agregar_editorial.place(x=500, y=300)
        self.btn_eliminar_editorial = Button(self.frame_editorial, text="Eliminar",state="disabled", font=(self.config["font-family"], self.config["btn-font-size"]), width=self.config["btn-size"], command=self.eliinar_editorial)
        self.btn_eliminar_editorial.place(x=500, y=350)
        self.btn_reset_editorial = Button(self.frame_editorial, text="Reset", font=(self.config["font-family"], self.config["btn-font-size"]), width=self.config["btn-size"], command=self.reset_editorial)
        self.btn_reset_editorial.place(x=500, y=400)
        self.btn_back_editorial = Button(self.frame_editorial, text="Volver", font=(self.config["font-family"], self.config["btn-font-size"]), width=15, command=self.back_tab_autores)
        self.btn_back_editorial.place(x=350, y=500)
        self.btn_next_editorial = Button(self.frame_editorial, text="Siguiente", font=(self.config["font-family"],self.config["btn-font-size"]), state="disabled",width=15, command=self.next_tab_editoriak)
        self.btn_next_editorial.place(x=730, y=500)

        """FRAME DE ARTICULOS"""
        self.frame_articulos = Frame(self.tab_articulos, background=self.config["background-color"])
        self.frame_articulos.place(x=0, y=0, width=1000, height=600)
        self.list_articulos = Listbox(self.frame_articulos, background=self.config["listbox-background-color"], font=(self.config["font-family"], self.config["font-size"]), width=30, height=25)
        self.list_articulos.place(x=10, y=10)
        self.load_articulos_de_autores()
        self.lbl_articulo_nombre = Label(self.frame_articulos, text="Nombre", background=self.config["background-color"], font=(self.config["font-family"], self.config["lbl-font-size"]), foreground=self.config["foreground"])
        self.lbl_articulo_nombre.place(x=600, y=10)
        self.entry_articulo_nombre = Entry(self.frame_articulos, font=(self.config["font-family"], self.config["entry-font-size"]), width=30)
        self.entry_articulo_nombre.place(x=450, y=45)
        self.lbl_articulo_ano = Label(self.frame_articulos, text="Año", background=self.config["background-color"], font=(self.config["font-family"], self.config["lbl-font-size"]), foreground=self.config["foreground"])
        self.lbl_articulo_ano.place(x=600, y=100)
        self.entry_articulo_ano = Entry(self.frame_articulos, font=(self.config["font-family"], self.config["entry-font-size"]), width=30)
        self.entry_articulo_ano.place(x=450, y=135)
        self.lbl_articulo_lugar = Label(self.frame_articulos, text="Lugar", background=self.config["background-color"], font=(self.config["font-family"], self.config["lbl-font-size"]), foreground=self.config["foreground"])
        self.lbl_articulo_lugar.place(x=600, y=190)
        self.entry_articulo_lugar = Entry(self.frame_articulos, font=(self.config["font-family"], self.config["entry-font-size"]), width=30)
        self.entry_articulo_lugar.place(x=450, y=225)
        self.lbl_numero = Label(self.frame_articulos, text="Numero", background=self.config["background-color"], font=(self.config["font-family"], self.config["lbl-font-size"]), foreground=self.config["foreground"])
        self.lbl_numero.place(x=600, y=280)
        self.entry_numero = Entry(self.frame_articulos, font=(self.config["font-family"], self.config["entry-font-size"]), width=30)
        self.entry_numero.place(x=450, y=315)
        self.btn_agregar_articulo = Button(self.frame_articulos, text="Agregar", font=(self.config["font-family"], self.config["btn-font-size"]), width=self.config["btn-size"])
        self.btn_agregar_articulo.place(x=500, y=370)
        self.btn_eliminar_articulo = Button(self.frame_articulos, text="Eliminar", state="disabled", font=(self.config["font-family"], self.config["btn-font-size"]), width=self.config["btn-size"])
        self.btn_eliminar_articulo.place(x=500, y=420)
        self.btn_reset_articulo = Button(self.frame_articulos, text="Reset", font=(self.config["font-family"], self.config["btn-font-size"]), width=self.config["btn-size"])
        self.btn_reset_articulo.place(x=500, y=470)
        self.btn_back_articulo = Button(self.frame_articulos, text="Volver", font=(self.config["font-family"], self.config["btn-font-size"]), width=15)
        self.btn_back_articulo.place(x=350, y=520)
        self.btn_next_articulo = Button(self.frame_articulos, text="Siguiente",  state="disabled",font=(self.config["font-family"], self.config["btn-font-size"]), width=15)
        self.btn_next_articulo.place(x=730, y=520)

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

    def agregar_autor(self):
        """primero miramos si los campos estan vacios"""
        self.entry_nombre.configure(highlightbackground="black")
        self.entry_apellido1.configure(highlightbackground="black")
        self.entry_apellido2.configure(highlightbackground="black")
        selected_indices = self.list_autores.curselection()
        if self.entry_nombre.get() == "" or self.entry_apellido1.get() == "" or self.entry_apellido2.get() == "" and len(selected_indices) == 1:
            messagebox.showerror("Error", "No se pueden dejar campos vacios")
            if self.entry_nombre.get() == "":
                self.entry_nombre.configure(highlightbackground="red")
            if self.entry_apellido1.get() == "":
                self.entry_apellido1.configure(highlightbackground="red")
            if self.entry_apellido2.get() == "":
                self.entry_apellido2.configure(highlightbackground="red")
            logging.error("No se pueden dejar campos vacios")
            self.entry_nombre.master.focus_set()
        else:
            autor = Autor(self.entry_nombre.get(), self.entry_apellido1.get(), self.entry_apellido2.get())
            """lo insertamos en la base de datos y si se inserta correctamente lo insertamos en la lista"""
            status = autor.insert()
            if status == 1:
                self.list_autores.delete(0, "end")
                autores = autor.SelectAurotes()
                for autor in autores:
                    self.list_autores.insert("end", autor[1]+" "+autor[2]+" "+autor[0])
                messagebox.showinfo("Exito", "Autor agregado correctamente")
                """quitamos el foco de los entry"""
                self.entry_nombre.master.focus_set()
                self.btn_eliminar_autor.configure(state="active")
                self.btn_next.configure(state="active")
                logging.info("Autor agregado correctamente")
            else:
                messagebox.showerror("Error", "No se pudo agregar el autor")
                logging.error("No se pudo agregar el autor")
                self.entry_nombre.master.focus_set()

    def eliminar_autor(self):
        if self.entry_nombre.get() != "" and self.entry_apellido1.get() != "" and self.entry_apellido2.get() != "":
            if messagebox.askyesno("Eliminar", "¿Estas seguro de que quieres eliminar este autor?"):
                autor = Autor(self.entry_nombre.get(), self.entry_apellido1.get(), self.entry_apellido2.get())
                status = autor.delete()
                if status == 1:
                    self.list_autores.delete(0, "end")
                    autores = autor.SelectAurotes()
                    for autor in autores:
                        self.list_autores.insert("end", autor[1]+" "+autor[2]+" "+autor[0])
                    self.entry_nombre.delete(0, "end")
                    self.entry_apellido1.delete(0, "end")
                    self.entry_apellido2.delete(0, "end")
                    messagebox.showinfo("Exito", "Autor eliminado correctamente")
                    self.entry_nombre.master.focus_set()
                    self.btn_eliminar_autor.configure(state="disabled")
                    self.btn_next.configure(state="disabled")
                    logging.info("Autor eliminado correctamente")
        else:
            messagebox.showerror("Error", "No se pueden dejar campos vacios")
            if self.entry_nombre.get() == "":
                self.entry_nombre.configure(highlightbackground="red")
            if self.entry_apellido1.get() == "":
                self.entry_apellido1.configure(highlightbackground="red")
            if self.entry_apellido2.get() == "":
                self.entry_apellido2.configure(highlightbackground="red")
            logging.error("No se pueden dejar campos vacios")
            self.entry_nombre.master.focus_set()
            return
    
    def click_list_autores(self):
        indexes = self.list_autores.curselection()
        if len(indexes) != 0:
            selected_indices = self.list_autores.curselection()
            selected_items = [self.list_autores.get(i) for i in selected_indices]
            nombres = ""
            apellido1 = ""
            apellido2 = ""
            for item in selected_items:
                item = item.split(" ")
                nombres = nombres + item[2] + " "
                apellido1 = apellido1 + item[0] + " "
                apellido2 = apellido2 + item[1] + " "
            self.entry_nombre.delete(0, "end")
            self.entry_nombre.insert(0, nombres)
            self.entry_apellido1.delete(0, "end")
            self.entry_apellido1.insert(0, apellido1)
            self.entry_apellido2.delete(0, "end")
            self.entry_apellido2.insert(0, apellido2)
            self.btn_eliminar_autor.configure(state="active")
            self.btn_next.configure(state="active")
            self.entry_nombre.master.focus_set()
            logging.info("Autor seleccionado correctamente")

        else:
            self.btn_eliminar_autor.configure(state="disabled")
            self.btn_next.configure(state="disabled")
            self.entry_nombre.delete(0, "end")
            self.entry_apellido1.delete(0, "end")
            self.entry_apellido2.delete(0, "end")
    
    def reset_autores(self):
        if messagebox.askyesno("Reset", "¿Estas seguro de que quieres borrar todos los autores?"):
            Autor("","","").reset()
            self.list_autores.delete(0, "end")
            self.entry_nombre.delete(0, "end")
            self.entry_apellido1.delete(0, "end")
            self.entry_apellido2.delete(0, "end")
            messagebox.showinfo("Exito", "Autores eliminados correctamente")
            self.entry_nombre.master.focus_set()
    
    def next_tab_autores(self):
        self.autor_cita = []
        selected_indices = self.list_autores.curselection()
        if len(selected_indices) == 0:
            messagebox.showerror("Error", "Debes seleccionar al menos un autor")
            logging.error("Debes seleccionar al menos un autor")
            return
        else:
            selected_items = [self.list_autores.get(i) for i in selected_indices]
            for i in selected_items:
                i = i.split(" ")
                autor = Autor(i[2], i[0], i[1])
                self.autor_cita.append(autor)
        self.tab_control.select(self.tab_editorial)
        logging.info("Pestaña siguiente seleccionada correctamente")
    
    def agregar_editorial(self):
        if self.entry_editorial_nombre.get() != "":
            editorial = Editorial(self.entry_editorial_nombre.get())
            status = editorial.insert()
            if status == 1:
                self.list_editorial.delete(0, "end")
                editoriales = editorial.SelectEditoriales()
                for editorial in editoriales:
                    self.list_editorial.insert("end", editorial[0])
                messagebox.showinfo("Exito", "Editorial agregada correctamente")
                self.entry_editorial_nombre.master.focus_set()
                logging.info("Editorial agregada correctamente")
        else:
            messagebox.showerror("Error", "No se pueden dejar campos vacios")
            self.entry_editorial_nombre.configure(highlightbackground="red")
            logging.error("No se pueden dejar campos vacios")
            self.entry_editorial_nombre.master.focus_set()
    
    def click_list_editorial(self):
        if self.list_editorial.curselection() == ():
            self.btn_eliminar_editorial.configure(state="disabled")
            self.btn_next_editorial.configure(state="disabled")
            self.entry_editorial_nombre.delete(0, "end")
            return
        else:
            editorial = self.list_editorial.get(self.list_editorial.curselection())
            self.entry_editorial_nombre.delete(0, "end")
            self.entry_editorial_nombre.insert(0, editorial)
            self.btn_eliminar_editorial.configure(state="active")
            self.btn_next_editorial.configure(state="active")
            self.entry_editorial_nombre.master.focus_set()

    def back_tab_autores(self):
        self.tab_control.select(self.tab_autores)
        logging.info("Pestaña anterior seleccionada correctamente")
    
    def eliinar_editorial(self):
        if messagebox.askyesno("Eliminar", "¿Estas seguro de que quieres eliminar esta editorial?"):
            editorial = Editorial(self.entry_editorial_nombre.get())
            status = editorial.delete()
            if status == 1:
                self.list_editorial.delete(0, "end")
                editoriales = editorial.SelectEditoriales()
                for editorial in editoriales:
                    self.list_editorial.insert("end", editorial[0])
                self.entry_editorial_nombre.delete(0, "end")
                messagebox.showinfo("Exito", "Editorial eliminada correctamente")
                self.entry_editorial_nombre.master.focus_set()
                self.btn_eliminar_editorial.configure(state="disabled")
                self.btn_next_editorial.configure(state="disabled")
                logging.info("Editorial eliminada correctamente")
            else:
                messagebox.showerror("Error", "No se pudo eliminar la editorial")
                logging.error("No se pudo eliminar la editorial")
                self.entry_editorial_nombre.master.focus_set()
    
    def reset_editorial(self):
        if messagebox.askyesno("Reset", "¿Estas seguro de que quieres borrar todas las editoriales?"):
            Editorial("").reset()
            self.list_editorial.delete(0, "end")
            self.entry_editorial_nombre.delete(0, "end")
            messagebox.showinfo("Exito", "Editoriales eliminadas correctamente")
            self.entry_editorial_nombre.master.focus_set()
    
    def next_tab_editoriak(self):
        self.editorial_cita = Editorial(self.entry_editorial_nombre.get())
        self.tab_control.select(self.tab_articulos)
    
    def load_articulos_de_autores(self):
        """primero, miramos la longitud de la lista de autores"""
        articulos_definitivos = []
        if len(self.autor_cita) == 1:
            articulos = Articulo("", "", "", "", "", "").select_articulo_nombre(self.autor_cita[0].nombre, self.autor_cita[0].apellido1, self.autor_cita[0].apellido2,self.editorial_cita.nombre)
            self.list_articulos.delete(0, "end")
            for articulo in articulos:
                self.list_articulos.insert("end", articulo[0])
        else:
            """cogemos los articulos del autor que seleccionemos, los guardamos en una lista y los comparamos con los demas autores"""
            for autor in self.autor_cita:
                articulos = Articulo("", "", "", "", "", "").select_articulo_nombre(autor.nombre, autor.apellido1, autor.apellido2,self.editorial_cita.nombre)
                """ahora miramos, si esta vacia la lista los metemos todos, si no estan, solo nos quedaremos con los comunes en la lista definitiva"""
                if articulos_definitivos == []:
                    """guardamos los nombres de los articulos en la lista"""
                    for articulo in articulos:
                        articulos_definitivos.append(articulo[0])
                else:
                    """guardamos en una lista temporal los articulos de este autor y en la lista defintiva nos quedamos con los articulos que esten en ambas listas"""
                    articulos_temporales = []
                    for articulo in articulos:
                        articulos_temporales.append(articulo[0])
                    articulos_definitivos = list(set(articulos_definitivos) & set(articulos_temporales))

            self.list_articulos.delete(0, "end")
            for articulo in articulos_definitivos:
                self.list_articulos.insert("end", articulo)

