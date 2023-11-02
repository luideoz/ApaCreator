#DBMANAGER 
import sqlite3 as sql

class DBManager:
    def __init__():
        pass
    
    def insert_delete_reset(**args) -> bool:
        conn = sql.connect("BBDD/"+str(args[0]) + ".db")
        cursor = conn.cursor()
        cursor.execute(args[1])
        conn.commit()
        conn.close()
    
    def select(**args) -> list:
        conn = sql.connect("BBDD/"+str(args[0]) + ".db")
        cursor = conn.cursor()
        cursor.execute(args[1])
        rows = cursor.fetchall()
        conn.close()
        return rows
        
        