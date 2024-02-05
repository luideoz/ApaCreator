from Persistencia.DBManager import DBManager

class EditorialDAO:
    
    def __init__(self):
        pass
    
    def SelectEditoriales(self) -> list:
        agent = DBManager()
        editoriales = agent.select("editoriales", "SELECT * FROM editoriales")
        return editoriales

    def SelectEditorial(self,*args) -> list:
        agent = DBManager()
        editorial = agent.select("editoriales", "SELECT * FROM editoriales WHERE nombre = '"+str(args[0])+"'")
        return editorial
    
    def insert(self, nombre) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("editoriales", "INSERT INTO editoriales (nombre) VALUES ('"+nombre+"')", None)
        return state

    def delete(self,nombre) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("editoriales", "DELETE FROM editoriales WHERE nombre = '"+nombre+"'", None)
        return state

    def reset(self) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("editoriales", "DELETE FROM editoriales")
        return state
    