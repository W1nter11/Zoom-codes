import sqlite3

def createdatabase():
    #freespace = [("", "", "")]
    with sqlite3.connect('data.sqlite') as db:
        cursor = db.cursor()
        query = (" CREATE TABLE IF NOT EXISTS zoomcodes(lesson TEXT, code TEXT, password TEXT)  ")
        cursor.execute(query)
        db.commit()
        print("Nice")
    '''with sqlite3.connect('data.sqlite') as db:
        cursor = db.cursor()
        query = """ INSERT INTO zoomcodes(lesson, code, password) VALUES (?, ?, ?); """
        cursor.executemany(query, freespace)
        db.commit()
        print("Nice")'''

def addtodatabase():
    ing_l = (input('Which lesson you want to add? '))
    ing_c = (input('Conferation code :  '))
    ing_p = (input('Conferation password : '))
    input_data = [(ing_l, ing_c, ing_p )]
    with sqlite3.connect('data.sqlite') as db:
        cursor = db.cursor()
        query = (" INSERT INTO zoomcodes(lesson, code, password) VALUES (?, ?, ?)")
        cursor.executemany(query, input_data)
        db.commit()
        print("Nice")
def deletefromdatabase():
    with sqlite3.connect('data.sqlite') as db:
            cursor = db.cursor()
            query = ("DELETE FROM zoomcodes")
            cursor.execute(query)
            db.commit()
            print("Nice")

def droptable():
    with sqlite3.connect('data.sqlite') as db:
        cursor = db.cursor()
        query = ("DROP TABLE zoomcodes")
        cursor.execute(query)
        db.commit()
        print("Nice")

def readtable():
    with sqlite3.connect('data.sqlite') as db:
        cursor = db.cursor()
        query = cursor.execute("SELECT lesson, code, password FROM zoomcodes").fetchall()
        print(query)


readtable()