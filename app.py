from flask import Flask, render_template, url_for
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('canciones.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nombre, artista, archivo FROM canciones")
    canciones = cursor.fetchall()
    conn.close()
    return render_template('index.html', canciones=canciones)

if __name__ == '__main__':
    app.run(debug=True)
