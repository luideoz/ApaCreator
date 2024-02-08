from Persistencia.DBManager import DBManager

class EditorialDAO:
    
    def __init__(self):
        pass
    
    def SelectEditoriales(self) -> list:
        agent = DBManager()
        editoriales = agent.select("articulos", "SELECT * FROM editoriales", None)
        return editoriales

    def SelectEditorial(self,*args) -> list:
        agent = DBManager()
        editorial = agent.select("articulos", "SELECT * FROM editoriales WHERE nombre = '"+str(args[0])+"'", None)
        return editorial
    
    def insert(self, nombre) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("articulos", "INSERT INTO editoriales (nombre) VALUES ('"+nombre+"')", None)
        return state

    def delete(self,nombre) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("articulos", "DELETE FROM editoriales WHERE nombre = '"+nombre+"'", None)
        return state

    def reset(self) -> int:
        agent = DBManager()
        state = agent.insert_delete_reset("articulos", "DELETE FROM editoriales", None)
        return state
    