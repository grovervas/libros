from tkinter import *
import backend

def get_select_fila(event):
    global tupla
    index = list1.curselection()[0]
    tupla = list1.get(index)
    e1.delete(0, END)
    e1.insert(END,tupla[1])
    e2.delete(0, END)
    e2.insert(END,tupla[2])
    e3.delete(0, END)
    e3.insert(END,tupla[3])
    e4.delete(0, END)
    e4.insert(END,tupla[4])

def ver_command():
    list1.delete(0, END)
    for row in backend.ver():
        list1.insert(END, row)

def buscar_command():
    list1.delete(0, END)
    for row in backend.buscar(titulo.get(), autor.get(), year.get(), isbn.get()):
        list1.insert(END, row)

def insert_command():
    backend.insertar(titulo.get(), autor.get(), year.get(), isbn.get())
    ver_command()

def delete_command():
    backend.eliminar(tupla[0])
    ver_command()

def update_command():
    backend.update(tupla[0], titulo.get(), autor.get(), year.get(), isbn.get())
    ver_command()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

window = Tk()

window.wm_title("Libros")

l1 = Label(window, text="Titulo")
l1.grid(row=0, column=0)

l2 = Label(window, text="Autor")
l2.grid(row=0, column=2)

l3 = Label(window, text="Año")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

titulo = StringVar()
e1 = Entry(window,textvariable=titulo)
e1.grid(row=0, column=1)

autor = StringVar()
e2 = Entry(window,textvariable=autor)
e2.grid(row=0, column=3)

year = StringVar()
e3 = Entry(window,textvariable=year)
e3.grid(row=1, column=1)

isbn = StringVar()
e4 = Entry(window,textvariable=isbn)
e4.grid(row=1, column=3)

list1 = Listbox(window, height=6, width=35)
list1.grid(row=2,column=0, columnspan=2, rowspan=6)

sb1 = Scrollbar(window)
sb1.grid(row=2,column=2, rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind("<<ListboxSelect>>", get_select_fila)

b1 = Button(window, text="Ver todos", width=12, command=ver_command)
b1.grid(row=2, column=3)

b2 = Button(window, text="Buscar", width=12, command=buscar_command)
b2.grid(row=3, column=3)

b3 = Button(window, text="Agregar", width=12, command=insert_command)
b3.grid(row=4, column=3)

b4 = Button(window, text="Actualizar", width=12, command=update_command)
b4.grid(row=5, column=3)

b5 = Button(window, text="Eliminar", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6 = Button(window, text="Cerrar", width=12, command=window.destroy)
b6.grid(row=7, column=3)


window.mainloop()
