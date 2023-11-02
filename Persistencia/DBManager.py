#DBMANAGER 
import sqlite3 as sql

class DBManager:
    def __init__():
        pass
    
    def insert_delete_reset(**args) -> int:
        conn = sql.connect("BBDD/"+str(args[0]) + ".db")
        cursor = conn.cursor()
        try:
            cursor.execute(args[1])
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
    
    def select(**args) -> list:
        conn = sql.connect("BBDD/"+str(args[0]) + ".db")
        cursor = conn.cursor()
        cursor.execute(args[1])
        rows = cursor.fetchall()
        conn.close()
        return rows
        
        