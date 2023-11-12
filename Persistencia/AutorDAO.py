from Persistencia.DBManager import DBManager

class AutorDAO:
    def __init__(self):
        pass
        
    def SelectAurotes(self) -> list:
        agent = DBManager()
        autores = agent.select("autores", "SELECT * FROM autores")
        return autores
    
    def SelectAutor(self,*args) -> list:
        agent = DBManager()
        autor = agent.select("autores", "SELECT * FROM autores WHERE nombre = '"+str(args[0])+"' AND apellido1 = '"+str(args[1])+"' AND apellido2 = '"+str(args[2])+"'")
        return autor
    
    def insert(self,*args) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("autores", "INSERT INTO autores (nombre, apellido1, apellido2) VALUES ('"+str(args[0])+"','"+str(args[1])+'","'+str(args[2])+"',")
        
    def delete(self,*args) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("autores", "DELETE FROM autores WHERE nombre = '"+str(args[0])+"' AND apellido1 = '"+str(args[1])+"' AND apellido2 = '"+str(args[2])+"'")
    
    def reset(self) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("autores", "DELETE FROM autores")