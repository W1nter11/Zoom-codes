import sqlite3

def createdatabase():
    with sqlite3.connect('main/data.sqlite') as db:
        cursor = db.cursor()
        query = """ CREATE TABLE IF NOT EXISTS zoomcodes(id INTEGER, lesson TEXT, code INTEGER, password TEXT)  """
        cursor.execute(query)



createdatabase()









#with sqlite3.connect('main/data.sqlite') as db:
#        cursor = db.cursor()
#        query1 = """ DROP TABLE zoomcodes """
#        cursor.execute(query1)
