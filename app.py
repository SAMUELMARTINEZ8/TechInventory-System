from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# 🔑 LLAVE SECRETA
app.secret_key = os.urandom(24)

# 🔒 CONFIGURACIÓN DE BASE DE DATOS
# ⚠️ IMPORTANTE: Cambia 'tech_inventory' por el nombre REAL que le pusiste en MySQL Workbench
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '', 
    'database': 'db.sql'  
}

def obtener_conexion():
    return mysql.connector.connect(**db_config)

# --- RUTA DE REGISTRO DE USUARIOS ---
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    # Si ya está logueado, lo mandamos al dashboard
    if 'user_id' in session:
        return redirect(url_for('index'))
    
    error = None
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']
        
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        
        # 1. Verificar si el correo ya existe
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        usuario_existente = cursor.fetchone()
        
        if usuario_existente:
            error = "⚠️ Ese correo ya está registrado."
            conn.close()
        else:
            # 2. Encriptar la contraseña (Seguridad ante todo)
            password_hash = generate_password_hash(password)
            
            # 3. Guardar en la base de datos
            cursor.execute("INSERT INTO usuarios (nombre, email, password_hash) VALUES (%s, %s, %s)", 
                         (nombre, email, password_hash))
            conn.commit()
            conn.close()
            
            # 4. Éxito: Mandarlo al login para que entre
            return redirect(url_for('login'))
            
    return render_template('registro.html', error=error)

# --- MIDDLEWARE DE SEGURIDAD ---
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# --- RUTAS PRINCIPALES ---
@app.route('/')
@login_required
def index():
    # 1. Conectamos
    conn = obtener_conexion()
    cursor = conn.cursor()
    
    # 2. Buscamos los productos
    cursor.execute("SELECT * FROM productos")
    mis_productos = cursor.fetchall()
    
    conn.close()
    
    # 3. Enviamos los productos al HTML
    return render_template('index.html', 
                         nombre_usuario=session.get('user_name'), 
                         productos=mis_productos)

# --- RUTA PARA ELIMINAR PRODUCTO ---
@app.route('/eliminar/<int:id>')
@login_required
def eliminar_producto(id):
    conn = obtener_conexion()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id = %s", (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index')) # Redirige a la función 'index' de arriba

# --- RUTA PARA EDITAR PRODUCTO (GET y POST) ---
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar_producto(id):
    conn = obtener_conexion()
    # Usamos dictionary=True para poder llamar a los campos por nombre (p['nombre'])
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        # 1. Recibimos los datos nuevos del formulario
        nombre = request.form['nombre']
        categoria = request.form['categoria']
        precio = request.form['precio']
        stock = request.form['stock']
        
        # 2. Actualizamos la base de datos
        sql = "UPDATE productos SET nombre=%s, categoria=%s, precio=%s, stock=%s WHERE id=%s"
        cursor.execute(sql, (nombre, categoria, precio, stock, id))
        conn.commit()
        conn.close()
        
        # 3. Regresamos al dashboard
        return redirect(url_for('index'))
        
    # Si es GET (al entrar a la página):
    # Buscamos el producto para mostrárselo al usuario
    cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
    producto = cursor.fetchone()
    conn.close()
    
    return render_template('editar.html', p=producto)

# RUTA: Página de Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('index')) # Corregido: redirige a 'index'
        
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            session['user_name'] = user['nombre']
            return redirect(url_for('index'))
        else:
            error = '❌ Email o contraseña incorrectos.'
            
    return render_template('login.html', error=error)

# RUTA: Cerrar Sesión
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# --- RUTAS API (Opcionales para el registro asíncrono) ---
@app.route('/api/productos', methods=['POST'])
@login_required
def add_producto():
    nuevo_prod = request.json
    conn = obtener_conexion()
    cursor = conn.cursor()
    sql = "INSERT INTO productos (nombre, categoria, precio, stock) VALUES (%s, %s, %s, %s)"
    valores = (nuevo_prod['nombre'], nuevo_prod['categoria'], nuevo_prod['precio'], nuevo_prod['stock'])
    cursor.execute(sql, valores)
    conn.commit()
    conn.close()
    return jsonify({"mensaje": "OK"}), 201
        
if __name__ == '__main__':
    app.run(debug=True, port=5000)