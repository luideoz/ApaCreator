from Persistencia.DBManager import DBManager

class AutorDAO:
    def __init__(self):
        pass
        
    def SelectAurotes(self) -> list:
        agent = DBManager()
        autores = agent.select("autores", "SELECT * FROM autor ORDER BY apellido1, apellido2, nombre")
        return autores
    
    def SelectAutor(self,nombre,apellido1,apellido2) -> list:
        agent = DBManager()
        autor = agent.select("autores", "SELECT * FROM autores WHERE nombre = '"+nombre+"' AND apellido1 = '"+apellido1+"' AND apellido2 = '"+apellido2+"'")
        return autor
    
    def insert(self,nombre,apellido1,apellido2) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("autores", "INSERT INTO autor (nombre, apellido1, apellido2) VALUES (?, ?, ?)", (nombre, apellido1, apellido2))
        return state
        
    def delete(self,nombre,apellido1,apellido2) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("autores", "DELETE FROM autor WHERE nombre = ? AND apellido1 = ? AND apellido2 = ?", (nombre, apellido1, apellido2))
        return state
    
    def reset(self) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("autores", "DELETE FROM autores")
        return state