import sqlite3
# ------------------------
from tkinter import Tk, Toplevel, Label, Entry, Button, messagebox
from tkinter import ttk
# ------------------------
from main import save_note
from main import exclude_note

root = Tk()

# ------------------------------------------------------------------------------------------

def create_note(root):

    window = Toplevel(root)
    window.title('Create note')

    id_label = Label(window, text='ID', font=('', 10)).grid(column=0, row=0)
    id_entry = Entry(window, width=40, font=('', 10))
    id_entry.grid(column=1, row=0)

    title_label = Label(window, text='Title', font=('', 10)).grid(column=0, row=1)
    title_entry = Entry(window, width=40, font=('', 10))
    title_entry.grid(column=1, row=1)

    description_label = Label(window, text='Description', font=('', 10)).grid(column=0, row=2)
    description_entry = Entry(window, width=40, font=('', 10))
    description_entry.grid(column=1, row=2)

    time_label = Label(window, text='Time', font=('', 10)).grid(column=0, row=3)
    time_entry = Entry(window, width=40, font=('', 10))
    time_entry.grid(column=1, row=3)

    def save_and_destroy():


        try:

            while True:

                time = time_entry.get().replace(':', '')

                while True:
                    if len(time) == 4:

                        try:
                            int(time)
                            break

                        except:
                            messagebox.showerror(title='Erro no horário', message='Digite o horário novamente.')

                    else:
                        messagebox.showerror(title='Erro no horário', message='Digite o horário novamente')

                if len(description_entry.get()) and len(title_entry.get()) < 31:
                    print(len(description_entry.get()) and len(title_entry.get()))
                    print(id_entry.get(), title_entry.get(), description_entry.get(), time_entry.get())
                    save_note(id_entry.get(), title_entry.get(), description_entry.get(), time_entry.get())
                    window.destroy()
                    frm.destroy()
                    main_page(root)
                    break

                else:
                    messagebox.showerror(title='Erro', message='O titulo e a descrição devem ter menos que 29 caracteres.')
                    break

        except sqlite3.IntegrityError:
            messagebox.showerror(title='Erro no ID', message='Já existe uma tarefa com esse ID.')

        except sqlite3.OperationalError:
            messagebox.showerror(title='Erro no ID', message='O ID deve ser composto apenas por números.')

    criar_btn = Button(window, text='Criar', width=35, font=('', 10), command=save_and_destroy).grid(column=1, row=4)


def create_note_and_destroy_main_page():
    create_note(root)

# -------------------------------------------------------------------------------------------------------------------------------------

def delete_and_destroy_main_page(id):
    exclude_note(id)
    print(id)
    frm.destroy()
    main_page(root)


# -------------------------------------------------------------------------------------------
def call_connection():

    # creating the connection and the cursor
    con = sqlite3.connect('notes.db')
    cur = con.cursor()
    cont = 1

    for task in cur.execute('SELECT * FROM notes'):

        def action(x=task[0]):
            return delete_and_destroy_main_page(x)

        Label(frm, text=task[0], width=20).grid(column=0, row=cont, padx=10)
        Label(frm, text=task[1], width=25).grid(column=1, row=cont, padx=20)
        Label(frm, text=task[2], width=25).grid(column=2, row=cont, padx=20)
        Label(frm, text=task[3], width=25).grid(column=3, row=cont, padx=20)

        Button(frm, text='x', command=action).grid(column=4, row=cont)

        cont += 1

    return cont

# ------------------------------------------------------------------------------------------

def main_page(root):

    root.title('Notes app')
    global frm
    frm = ttk.Frame(root, padding=10)
    frm.grid()

    # Edit note button
    # ttk.Button(frm, text="Edit note", command=root.destroy, width=30).grid(column=2, row=0, columnspan=2)

    # Delete note button
    # ttk.Button(frm, text="Delete note", command=delete_and_destroy_main_page, width=30).grid(column=2, row=0)

    # Quit
    # ttk.Button(frm, text="Quit", command=root.destroy, width=30).grid(column=3, row=0)
    # ------------------------------------------------------------------------------------------

    Label(frm, text='ID', width=20, background='red', justify='center').grid(column=0, row=0, padx=10)
    Label(frm, text='Title', width=25, background='red').grid(column=1, row=0)
    Label(frm, text='Description', width=25, background='red').grid(column=2, row=0)
    Label(frm, text='Time', width=25, background='red').grid(column=3, row=0)

    cont = call_connection()

    # Create note button
    Button(frm, text='New task', width=113, bg='red', command=create_note_and_destroy_main_page).grid(column=0, row=int(cont+1), columnspan=4, pady=5)

# -------------------------------------------------------------------------------------------

    root.mainloop()


main_page(root)
