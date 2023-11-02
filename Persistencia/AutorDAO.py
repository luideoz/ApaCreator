from Persistencia.DBManager import DBManager

class AutorDAO:
    def __init__(self):
        pass
        
    def SelectAurotes(self) -> list:
        agent = DBManager()
        autores = agent.select("autores", "SELECT * FROM autores")
        return autores
    
    def SelectAutor(self,**args) -> list:
        agent = DBManager()
        autor = agent.select("autores", "SELECT * FROM autores WHERE nombre = '"+str(args[0])+"' AND apellido = '"+str(args[1])+"'")
        return autor
    
    def insert(self,**args) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("autores", "INSERT INTO autores (nombre, apellido) VALUES ('"+str(args[0])+"','"+str(args[1])+"')")
        
    def delete(self,**args) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("autores", "DELETE FROM autores WHERE nombre = '"+str(args[0])+"' AND apellido = '"+str(args[1])+"'")
    
    def reset(self) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("autores", "DELETE FROM autores")