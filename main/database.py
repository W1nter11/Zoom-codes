import sqlite3

def createdatabase():
    freespace = [("", "", "", "")]
    with sqlite3.connect('main/data.sqlite') as db:
        cursor = db.cursor()
        query = """ CREATE TABLE IF NOT EXISTS zoomcodes(id TEXT, lesson TEXT, code TEXT, password TEXT)  """
        cursor.execute(query)
    with sqlite3.connect('main/data.sqlite') as db:
        cursor = db.cursor()
        query = """ INSERT INTO zoomcodes(id, lesson, code, password) VALUES (?, ?, ?, ?); """
        cursor.executemany(query, freespace)
        db.commit()

def addtodatabase():
    ing_l = (input('Which lesson you want to add? '))
    ing_c = (input('Conferation code :  '))
    ing_p = (input('Conferation password : '))
    with sqlite3.connect('main/data.sqlite') as db:
        cursor = db.cursor()
        cursor.execute("SELECT max(rowid) from zoomcodes")
        ing_i = cursor.fetchone()[0]
    input_data = [(ing_i, ing_l, ing_c, ing_p )]
    with sqlite3.connect('main/data.sqlite') as db:
        cursor = db.cursor()
        query = """ INSERT INTO zoomcodes(id, lesson, code, password) VALUES (?, ?, ?, ?); """
        cursor.executemany(query, input_data)
        db.commit()
    print(ing_i)

def deletefromdatabase():
    with sqlite3.connect('main/data.sqlite') as db:
            cursor = db.cursor()
            query = """DELETE FROM zoomcodes"""
            cursor.execute(query)
            db.commit()

def droptable():
    with sqlite3.connect('main/data.sqlite') as db:
        cursor = db.cursor()
        query = """DROP TABLE zoomcodes"""
        cursor.execute(query)
        db.commit()

addtodatabase()