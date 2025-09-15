import sqlite3

# Conexión a la base de datos (se crea si no existe)
conn = sqlite3.connect('canciones.db')
cursor = conn.cursor()

# Crear tabla con todos los campos necesarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS canciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        artista TEXT NOT NULL,
        archivo TEXT NOT NULL
    )
''')

conn.commit()
conn.close()

print("Base de datos creada correctamente.")
