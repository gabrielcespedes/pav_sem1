import sqlite3

#cursor

conn = sqlite3.connect("usuarios_s1.db")

cursor = conn.cursor()

cursor.execute(
    """
    DELETE FROM 'usuarios';
    """
)

conn.commit()
conn.close()