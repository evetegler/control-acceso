from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    dato = request.form['dato']
    conn = get_db_connection()
    # Buscar por patente o rut
    vehiculo = conn.execute("SELECT * FROM accesos WHERE patente = ? OR rut_empresa = ? ORDER BY fecha DESC", (dato, dato)).fetchall()
    conn.close()
    return render_template('accesos.html', accesos=vehiculo)

@app.route('/proveedores')
def proveedores():
    conn = get_db_connection()
    proveedores = conn.execute("SELECT * FROM proveedores").fetchall()
    conn.close()
    return render_template('proveedores.html', proveedores=proveedores)

@app.route('/nuevo_proveedor', methods=['POST'])
def nuevo_proveedor():
    nombre = request.form['nombre']
    rut = request.form['rut']
    conn = get_db_connection()
    conn.execute("INSERT INTO proveedores (nombre, rut) VALUES (?, ?)", (nombre, rut))
    conn.commit()
    conn.close()
    return redirect('/proveedores')

@app.route('/registrar_acceso', methods=['POST'])
def registrar_acceso():
    patente = request.form['patente']
    rut_empresa = request.form['rut_empresa']
    observacion = request.form['observacion']
    conn = get_db_connection()
    conn.execute("INSERT INTO accesos (patente, rut_empresa, observacion, fecha) VALUES (?, ?, ?, datetime('now', 'localtime'))", (patente, rut_empresa, observacion))
    conn.commit()
    conn.close()
    return redirect('/')
