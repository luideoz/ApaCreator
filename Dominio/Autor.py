from Persistencia.AutorDAO import AutorDAO

class Autor:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.AutordDAO = AutorDAO()
    
    def insert(self) -> int:
        return self.AutordDAO.insert(self.nombre, self.apellido)
    
    def delete(self) -> int:
        return self.AutordDAO.delete(self.nombre, self.apellido)
    
    def reset(self) -> int:
        return self.AutordDAO.reset()
    
    def SelectAutor(self) -> list:
        return self.AutordDAO.SelectAutor(self.nombre, self.apellido)
    
    def SelectAurotes(self) -> list:
        return self.AutordDAO.SelectAurotes()