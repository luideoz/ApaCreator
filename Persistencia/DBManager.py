#DBMANAGER 
import sqlite3 as sql

class DBManager:
    
    def __init__(self):
        pass
    
    def insert_delete_reset(self,table,instruction,params) -> int:
        conn = sql.connect("BBDD/"+table+".db")
        cursor = conn.cursor()
        try:
            if params != None:
                cursor.execute(instruction,params)
            else:
                cursor.execute(instruction)
            conn.commit()
            conn.close()
            estado = 1
        except sql.OperationalError:
            estado = 0
        except sql.IntegrityError:
            estado = 0
        except sql.DatabaseError:
            estado = 0
        except sql.DataError:
            estado = 0
        except sql.NotSupportedError:
            estado = 0
        except sql.ProgrammingError:
            estado = 0
        return estado
    
    def select(self,table,instruction,params) -> list:
        conn = sql.connect("BBDD/"+table+ ".db")
        cursor = conn.cursor()
        if params == None:
            cursor.execute(instruction)
        else:
            cursor.execute(instruction,params)
        rows = cursor.fetchall()
        conn.close()
        return rows
        
        