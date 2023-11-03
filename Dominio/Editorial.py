from Persistencia.EditorialDAO import EditorialDAO

class Editorial:
    
    def __init__(self, nombre):
        self.__nombre__ = nombre
        self.__editorialDAO__ = EditorialDAO()
    
    def getNombre(self):
        return self.__nombre__
    
    def setNombre(self, nombre):
        self.__nombre__ = nombre
    
    def insert(self):
        return self.__editorialDAO__.insert(self.__nombre__)
    
    def delete(self):
        return self.__editorialDAO__.delete(self.__nombre__)
    
    def reset(self):
        return self.__editorialDAO__.reset()
    
    def SelectEditoriales(self):
        return self.__editorialDAO__.SelectEditoriales()
    
    def SelectEditorial(self):
        return self.__editorialDAO__.SelectEditorial(self.__nombre__)