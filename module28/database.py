import sqlite3
from pydanticnames import Name, NamesCreate



def create_connection():
    connection = sqlite3.connect("name.db")
    connection.row_factory = sqlite3.Row
    return connection

def create_table():
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL
        )
    """)
    connection.commit()
    connection.close()

def create_name(name: NamesCreate) -> int:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO name (name, surname) VALUES (?, ?)", (name.name, name.surname))
    connection.commit()
    book_id = cursor.lastrowid
    connection.close()
    return book_id

def read_name(name_id: int):
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM names WHERE id = ?", (name_id,))
    row = cursor.fetchone()
    connection.close()
    if row is None:
        return None
    return Name(id=row["id"], title=row["name"], author=row["surname"])
def update_name(name_id: int, name: NamesCreate) -> bool:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("UPDATE name SET title = ?, author = ? WHERE id = ?", (name.name, name.surname, name_id))
    connection.commit()
    updated = cursor.rowcount
    connection.close()
    return updated > 0


def delete_name(name_id: int) -> bool:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM name WHERE id = ?", (name_id,))
    connection.commit()
    deleted = cursor.rowcount
    connection.close()
    return deleted > 0

create_table()