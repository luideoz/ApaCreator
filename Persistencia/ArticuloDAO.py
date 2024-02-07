from Persistencia.DBManager import DBManager

class ArticuloDAO:
    
    def __init__(self):
        pass
    
    def select_articulo_nombre(self,nombreA, apellido1A, apellido2A, editorial):
        db = DBManager()
        query = "SELECT * from articulo WHERE editorial = ? AND nombre IN (SELECT nombre FROM autor_articulo WHERE nombreA = ? AND apellido1A = ? AND apellido2A = ?)"
        values = (editorial, nombreA, apellido1A, apellido2A)
        return db.select(query, values)