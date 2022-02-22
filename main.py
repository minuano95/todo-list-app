import os
import sqlite3


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

def save_note(id, note_title, note_description, note_time):
    # creating connection with the db
    con = sqlite3.connect('notes.db')
    # creating cursor
    cur = con.cursor()

    cur.execute(f"INSERT INTO notes VALUES ({id}, '{note_title}', '{note_description}', '{note_time}')")

    con.commit()
    con.close()

# create_note('Café', 'Fazer café')

# ------------------------------------------------------------------------------

# def edit_note(original_note_title,)


# ------------------------------------------------------------------------------

def exclude_note(id):
    # creating connection with the db
    con = sqlite3.connect('notes.db')
    # creating cursor
    cur = con.cursor()

    cur.execute(f"DELETE FROM notes WHERE id={id}")

    con.commit()
    con.close()