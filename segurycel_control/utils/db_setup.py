import sqlite3

conn = sqlite3.connect('../database.db')
c = conn.cursor()

# Tabla de proveedores
c.execute('''
    CREATE TABLE IF NOT EXISTS proveedores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        rut TEXT UNIQUE NOT NULL
    )
''')

# Tabla de accesos
c.execute('''
    CREATE TABLE IF NOT EXISTS accesos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patente TEXT NOT NULL,
        rut_empresa TEXT,
        observacion TEXT,
        fecha TEXT NOT NULL
    )
''')

conn.commit()
conn.close()
print("Base de datos creada.")
