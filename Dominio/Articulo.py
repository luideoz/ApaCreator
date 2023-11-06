from Persistencia.ArticuloDAO import ArticuloDAO

class Articulo:
    
    def __init(self,nombre,año,lugar,editorial,numero):
        self.nombre = nombre
        self.año = año
        self.lugar = lugar
        self.editorial = editorial
        self.numero = numero
    
    def insert(self) -> int:
        agente = ArticuloDAO()
        state = agente.insert(self.nombre, self.año, self.lugar, self.editorial, self.numero)
        return state
    
    def delete(self) -> int:
        agente = ArticuloDAO()
        state = agente.delete(self.nombre)
        return state
    
    def reset(self) -> int:
        agente = ArticuloDAO()
        state = agente.reset()
        return state
    
    def insertArticulo_Autor(self,autor) -> int:
        agente = ArticuloDAO()
        state = agente.insertArticulo_Autor(autor.nombre, autor.apellido, self.nombre)
        return state
    
    def deleteArticulo_Autor(self,autor) -> int:
        agente = ArticuloDAO()
        state = agente.deleteArticulo_Autor(autor.nombre, autor.apellido)
        return state
    
    def deleteArticulo_Autor_2(self) -> int:
        agente = ArticuloDAO()
        state = agente.deleteArticulo_Autor_2(self.nombre)
        return state
    
    def SelectArticulo(self) -> list:
        agente = ArticuloDAO()
        articulo = agente.SelectArticulo(self.nombre)
        return articulo
    
    def SelectArticulos(self) -> list:
        agente = ArticuloDAO()
        articulos = agente.SelectArticulos()
        return articulos
    
    def SelectAritulosAutor(self,autor) -> list:
        agente = ArticuloDAO()
        articulos = agente.SelectAritulosAutor(autor.nombre, autor.apellido)
        return articulos
    
    def resetArticulo_Autor(self) -> int:
        agente = ArticuloDAO()
        state = agente.resetArticulo_Autor()
        return state
    
    