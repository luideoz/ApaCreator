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
    
    def insert_articulo(self,editorial):
        return self.articuloDAO.insert_articulo(self.nombre,self.lugar,self.numero,self.ano,editorial)
    
    def insert_articulo_autor(self,nombre,nombreA,apellido1A,apellido2A):
        return self.articuloDAO.insert_articulo_autor(nombre,nombreA,apellido1A,apellido2A)
    
    def select_articulos(self):
        return self.articuloDAO.select_articulos()
    
    def select_articulo(self):
        return self.articuloDAO.select_articulo(self.nombre)
    
    def reset_articulo(self):
        return self.articuloDAO.reset_articulos()
    
    def reset_aritulo_autor(self):
        return self.articuloDAO.reset_articulos_autor()
    
    def delete_articulo(self):
        return self.articuloDAO.delete_articulo(self.nombre)
    
    def delete_articulo_autor(self,nombreA,apellido1A,apellido2A):
        return self.articuloDAO.delete_articulo_autor(self.nombre,nombreA,apellido1A,apellido2A)
    
    def delete_articulo_autor_con_nombre(self,nombreA,apellido1A,apellido2A):
        return self.articuloDAO.delete_articulo_autor_con_nombre(nombreA,apellido1A,apellido2A)
    
    def delete_articulo_sin_autor(self):
        return self.articuloDAO.delete_articulo_sin_autor()
    
    def delete_articulo_con_editorial(self,editorial):
        return self.articuloDAO.delete_articulo_con_editorial(editorial)
    
    def delete_articulos_autor_sin_articulo(self):
        return self.articuloDAO.delete_articulos_autor_sin_articulo()
    
    