from Persistencia.AutorDAO import AutorDAO

class Autor:
    def __init__(self, nombre, apellido1, apellido2):
        self.nombre = nombre
        self.apellido = apellido1
        self.apellido2 = apellido2
        self.AutordDAO = AutorDAO()
    
    def insert(self) -> int:
        return self.AutordDAO.insert(self.nombre, self.apellido, self.apellido2)
    
    def delete(self) -> int:
        return self.AutordDAO.delete(self.nombre, self.apellido, self.apellido2)
    
    def reset(self) -> int:
        return self.AutordDAO.reset()
    
    def SelectAutor(self) -> list:
        return self.AutordDAO.SelectAutor(self.nombre, self.apellido, self.apellido2)
    
    def SelectAurotes(self) -> list:
        return self.AutordDAO.SelectAurotes()