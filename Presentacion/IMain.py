from tkinter import *

class IMain:
    def __init__(self):
        self.window = Tk()
        self.window.title("Generador de Citas APA")
        icon = PhotoImage(file='media/libro-magico.png')
        self.window.iconphoto(False, icon)



        self.window.mainloop()