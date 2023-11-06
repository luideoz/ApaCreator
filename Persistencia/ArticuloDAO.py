from Persistencia.DBManager import DBManager

class ArticuloDAO:
    
    def __init__(self):
        pass
    
    def SelectArticulos(self) -> list:
        agent = DBManager()
        articulos = agent.select("articulos", "SELECT * FROM articulos")
        return articulos
    
    def SelectArticulo(self,*args) -> list:
        agent = DBManager()
        articulo = agent.select("articulos", "SELECT * FROM articulos WHERE nombre = '"+str(args[0])+"'")
        return articulo
    
    def SelectAritulosAutor(self,*args) -> list:
        agent = DBManager()
        list_articulos = agent.select("articulos_autor", "SELECT articulo from articulos_autor WHERE nombre_autor = '"+str(args[0])+"' AND apellido_autor = '"+str(args[1])+"'")
        return list_articulos
    
    def insert(self,*args) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("articulos","INSERT INTO articulos (nombre, año, lugar, editorial, numero) VALUES ('"+str(args[0])+"','"+int(args[1])+"','"+str(args[2])+"','"+str(args[3])+"','"+int(args[4])+"')")
        return state
    
    def insertArticulo_Autor(self,*args) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("articulos_autor","INSERT INTO articulos_autor (nombre_autor, apellido_autor, articulo) VALUES ('"+str(args[0])+"','"+str(args[1])+"','"+str(args[2])+"')")
        return state
    
    def delete(self,*args) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("articulos","DELETE FROM articulos WHERE nombre = '"+str(args[0])+"'")
        return state
    
    def deleteArticulo_Autor_1(self,*args) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("articulos_autor","DELETE FROM articulos_autor WHERE articulo = '"+str(args[0])+"'")
        return state
    
    def deleteArticulo_Autor_2(self,*args) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("articulos_autor","DELETE FROM articulos_autor WHERE nombre_autor = '"+str(args[0])+"' AND apellido_autor = '"+str(args[1])+"'")
        return state
    
    
    def reset(self) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("articulos","DELETE FROM articulos")
        return state
    
    def resetArticulo_Autor(self) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("articulos_autor","DELETE FROM articulos_autor")
        return state