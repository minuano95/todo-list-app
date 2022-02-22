import sqlite3

# creating connection with the db
con = sqlite3.connect('notes.db')

cur = con.cursor()

# cur.execute('CREATE TABLE notes ("id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "note_title" TEXT NOT NULL, "note_description" TEXT NOT NULL, note_time CHECK(typeof("note_title")="text" AND length("note_title")<=35))')


# for task in cur.execute('SELECT * FROM notes'):
#     print(task)

con.commit()
con.close()
