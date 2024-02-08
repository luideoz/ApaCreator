from Persistencia.DBManager import DBManager

class AutorDAO:
    def __init__(self):
        pass
        
    def SelectAurotes(self) -> list:
        agent = DBManager()
        autores = agent.select("articulos", "SELECT * FROM autores ORDER BY apellido1, apellido2, nombre", None)
        return autores
    
    def SelectAutor(self,nombre,apellido1,apellido2) -> list:
        agent = DBManager()
        autor = agent.select("articulos", "SELECT * FROM autores WHERE nombre = '"+nombre+"' AND apellido1 = '"+apellido1+"' AND apellido2 = '"+apellido2+"'", None)
        return autor
    
    def insert(self,nombre,apellido1,apellido2) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("articulos", "INSERT INTO autores (nombre, apellido1, apellido2) VALUES (?, ?, ?)", (nombre, apellido1, apellido2))
        return state
        
    def delete(self,nombre,apellido1,apellido2) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("articulos", "DELETE FROM autores WHERE nombre = ? AND apellido1 = ? AND apellido2 = ?", (nombre, apellido1, apellido2))
        return state
    
    def reset(self) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("articulos", "DELETE FROM autores", None)
        return state