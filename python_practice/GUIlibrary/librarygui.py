from tkinter import *
import sqlite3

from databa import delete, insert, search, update, view

def get_selected_row(event):
    global selected_tuple
    index = listbox.curselection()[0]
    selected_tuple = listbox.get(index)
    entry_title.delete(0, END)
    entry_title.insert(END, selected_tuple[1])
    entry_author.delete(0, END)
    entry_author.insert(END, selected_tuple[2])
    entry_year.delete(0, END)
    entry_year.insert(END, selected_tuple[3])
    entry_isbn.delete(0, END)
    entry_isbn.insert(END, selected_tuple[4])

def view_command():
    listbox.delete(0, END)
    for row in view():
        listbox.insert(END, row)

def search_command():
    listbox.delete(0, END)
    for row in search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        listbox.insert(END, row)

def add_command():
    insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    listbox.delete(0, END)
    listbox.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    delete(selected_tuple[0])

def update_command():
    update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())

window = Tk()
window.title("Library Management System")

label_title = Label(window, text="Title")
label_title.grid(row=0, column=0)

label_author = Label(window, text="Author")
label_author.grid(row=0, column=2)

label_year = Label(window, text="Year")
label_year.grid(row=1, column=0)

label_isbn = Label(window, text="ISBN")
label_isbn.grid(row=1, column=2)

title_text = StringVar()
entry_title = Entry(window, textvariable=title_text)
entry_title.grid(row=0, column=1)

author_text = StringVar()
entry_author = Entry(window, textvariable=author_text)
entry_author.grid(row=0, column=3)

year_text = StringVar()
entry_year = Entry(window, textvariable=year_text)
entry_year.grid(row=1, column=1)

isbn_text = StringVar()
entry_isbn = Entry(window, textvariable=isbn_text)
entry_isbn.grid(row=1, column=3)

listbox = Listbox(window, height=8, width=35)
listbox.grid(row=2, column=0, rowspan=6, columnspan=2)

scrollbar = Scrollbar(window)
scrollbar.grid(row=2, column=2, rowspan=6)

listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

listbox.bind('<<ListboxSelect>>', get_selected_row)

button_view_all = Button(window, text="View all", width=12, command=view_command)
button_view_all.grid(row=2, column=3)

button_search = Button(window, text="Search entry", width=12, command=search_command)
button_search.grid(row=3, column=3)

button_add = Button(window, text="Add entry", width=12, command=add_command)
button_add.grid(row=4, column=3)

button_update = Button(window, text="Update selected", width=12, command=update_command)
button_update.grid(row=5, column=3)

button_delete = Button(window, text="Delete selected", width=12, command=delete_command)
button_delete.grid(row=6, column=3)

button_close = Button(window, text="Close", width=12, command=window.destroy)
button_close.grid(row=7, column=3)

window.mainloop()
