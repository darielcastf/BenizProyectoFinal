import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), 'database', 'asistente.db')

def conectar():
    return sqlite3.connect(DB_PATH)

def crear_tablas():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        correo TEXT UNIQUE,
        edad INTEGER,
        ingreso_mensual REAL,
        objetivo TEXT
    );""")
    cur.execute("""CREATE TABLE IF NOT EXISTS productos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        entidad TEXT,
        tipo TEXT,
        tasa REAL,
        minimo REAL,
        descripcion TEXT
    );""")
    cur.execute("""CREATE TABLE IF NOT EXISTS recomendaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        producto_id INTEGER,
        razon TEXT,
        fecha DATETIME DEFAULT CURRENT_TIMESTAMP
    );""")
    conn.commit()
    conn.close()
    print('Tablas creadas en', DB_PATH)

if __name__ == '__main__':
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    crear_tablas()