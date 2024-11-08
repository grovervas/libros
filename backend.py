import sqlite3


def connect():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo text, autor text, year integer, isbn integer)")
    conn.commit()
    conn.close()

def insertar(titulo, autor, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO book VALUES(?,?,?,?)", (titulo, autor, year, isbn))
    conn.commit()
    conn.close()

def ver():
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book")
    rows = cur.fetchall()
    conn.close()
    return rows

def buscar(titulo="", autor="", year="", isbn=""):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM book WHERE titulo=? OR autor=? OR year=? OR isbn=?", (titulo, autor, year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def eliminar(id):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?", (id,))
    conn.commit()
    conn.close()

def update (id, titulo, autor, year, isbn):
    conn = sqlite3.connect("books.db")
    cur = conn.cursor()
    cur.execute("UPDATE book SET titulo=?, autor=?, year=?, isbn=? WHERE id=?", (titulo, autor, year, isbn, id))
    conn.commit()
    conn.close()

connect()
