import sqlite3

nombre = "All Eyez on Me"
artista = "2Pac"
archivo = "2Pac_-_All_Eyez_On_Me(256k).mp3" 

# Conexión a la base de datos
conn = sqlite3.connect('canciones.db')
cursor = conn.cursor()

# Insertar la canción en la tabla
cursor.execute('''
    INSERT INTO canciones (nombre, artista, archivo)
    VALUES (?, ?, ?)
''', (nombre, artista, archivo))

conn.commit()
conn.close()

print("Canción agregada correctamente.")
