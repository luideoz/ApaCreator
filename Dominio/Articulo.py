from Persistencia.ArticuloDAO import ArticuloDAO

class Articulo:
    
    def __init__(self,nombre,ano,lugar,editorial,numero):
        self.nombre = nombre
        self.ano = ano
        self.lugar = lugar
        self.numero = numero
        self.articuloDAO = ArticuloDAO()
    
    def select_articulo_nombre(self,nombreA,apellido1A,apellido2A,editorial):
        return self.articuloDAO.select_articulo_nombre(nombreA,apellido1A,apellido2A,editorial)
    
    