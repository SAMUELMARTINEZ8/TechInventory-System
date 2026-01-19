from flask import Flask, render_template, request, jsonify, redirect, url_for, session
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

# 🔑 LLAVE SECRETA (Necesaria para las sesiones de login)
# En producción, esto debe ser un código largo y secreto.
app.secret_key = os.urandom(24)

# 🔒 CONFIGURACIÓN DE BASE DE DATOS (Verifica tu nombre de DB)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'db.sql' # Asegúrate de que este nombre sea el correcto
}

def obtener_conexion():
    return mysql.connector.connect(**db_config)

# --- MIDDLEWARE DE SEGURIDAD ---
# Esta función "protege" las rutas. Si no estás logueado, te manda al login.
def login_required(f):
    from functools import wraps
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# --- RUTAS PRINCIPALES ---

# RUTA: Página de Login (GET para verla, POST para enviar datos)
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Si ya está logueado, mandarlo al dashboard
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
        
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        conn = obtener_conexion()
        cursor = conn.cursor(dictionary=True)
        # Buscamos al usuario por su email
        cursor.execute("SELECT * FROM usuarios WHERE email = %s", (email,))
        user = cursor.fetchone()
        conn.close()

        # Verificamos: 1. Si el usuario existe, 2. Si la contraseña coincide con el hash
        if user and check_password_hash(user['password_hash'], password):
            # ¡Login exitoso! Guardamos datos en la sesión
            session['user_id'] = user['id']
            session['user_name'] = user['nombre']
            return redirect(url_for('dashboard'))
        else:
            error = '❌ Email o contraseña incorrectos.'
            
    return render_template('login.html', error=error)

# RUTA: Dashboard (Protegida con @login_required)
@app.route('/')
@login_required
def dashboard():
    # Pasamos el nombre del usuario a la plantilla
    return render_template('index.html', nombre_usuario=session['user_name'])

# RUTA: Cerrar Sesión
@app.route('/logout')
def logout():
    session.clear() # Borramos la sesión
    return redirect(url_for('login'))

# --- RUTAS DE LA API (Inventario) ---
# También deberían estar protegidas en un sistema real

@app.route('/api/productos', methods=['GET'])
@login_required # Protegemos la API también
def get_productos():
    conn = obtener_conexion()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM productos ORDER BY id DESC")
    productos = cursor.fetchall()
    conn.close()
    return jsonify(productos)

@app.route('/api/productos', methods=['POST'])
@login_required # Protegemos la API también
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

# --- HERRAMIENTA PARA CREAR EL PRIMER USUARIO ---
# Descomenta estas líneas UNA SOLA VEZ, ejecuta el programa, y vuélvelas a comentar.
# Esto creará tu usuario administrador.

"""
@app.route('/crear-admin')
def crear_admin():
    password_plano = 'admin123' 
    hashed_pw = generate_password_hash(password_plano) # Tu Python calcula el hash correcto aquí
    
    conn = obtener_conexion()
    cursor = conn.cursor()
    try:
        # Primero borramos cualquier rastro anterior para evitar errores
        cursor.execute("DELETE FROM usuarios WHERE email = 'admin@tech.com'")
        
        # Insertamos el nuevo usuario limpio
        cursor.execute("INSERT INTO usuarios (email, password_hash, nombre) VALUES (%s, %s, %s)",
                       ('admin@tech.com', hashed_pw, 'Samuel Admin'))
        conn.commit()
        return "✅ ¡LISTO! Usuario creado. La contraseña admin123 ahora sí funcionará."
    except Exception as e:
        return f"Error: {e}"
    finally:
        conn.close()
"""
        
if __name__ == '__main__':
    app.run(debug=True, port=5000)