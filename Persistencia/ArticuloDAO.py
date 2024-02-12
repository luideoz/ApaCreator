from Persistencia.DBManager import DBManager

class ArticuloDAO:
    
    def __init__(self):
        pass
    
    def select_articulo_nombre(self,nombreA, apellido1A, apellido2A, editorial):
        db = DBManager()
        query = "SELECT * from articulos WHERE editorial = ? AND nombre IN (SELECT nombre FROM articulos_autor WHERE nombreA = ? AND apellido1A = ? AND apellido2A = ?)"
        values = (editorial, nombreA, apellido1A, apellido2A)
        return db.select("articulos",query, values)
    
    def select_articulos(self):
        db = DBManager()
        query = "SELECT * from articulos"
        return db.select("articulos",query,None)

    def insert_articulo(self,nombre,lugar,numero,ano,editorial):
        db = DBManager()
        query = "INSERT INTO articulos(nombre,lugar,año,numero,editorial) VALUES(?,?,?,?,?)"
        values = (nombre,lugar,ano,numero,editorial)
        return db.insert_delete_reset("articulos",query, values)

    def insert_articulo_autor(self,nombre,nombreA, apellido1A, apellido2A):
        db = DBManager()
        query = "INSERT INTO articulos_autor(nombre,nombreA,apellido1A,apellido2A) VALUES(?,?,?,?)"
        values = (nombre,nombreA,apellido1A,apellido2A)
        return db.insert_delete_reset("articulos",query, values)
    
    def reset_articulos(self):
        db = DBManager()
        query = "DELETE FROM articulos"
        return db.insert_delete_reset("articulos",query,None)

    def reset_articulos_autor(self):
        db = DBManager()
        query = "DELETE FROM articulos_autor"
        return db.insert_delete_reset("articulos",query,None)