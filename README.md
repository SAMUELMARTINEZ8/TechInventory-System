# ⚡ TechInventory System V2.0

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Framework-red?style=for-the-badge&logo=flask)
![MySQL](https://img.shields.io/badge/MySQL-Database-orange?style=for-the-badge&logo=mysql)
![Frontend](https://img.shields.io/badge/UI-Minimalist%20Apple%20Style-lightgrey?style=for-the-badge)

Un sistema **Full Stack** de gestión de inventarios empresariales. Esta versión incluye autenticación segura, protección de rutas y una interfaz gráfica moderna y minimalista.

## 🚀 Características Principales

### 🔒 Seguridad & Backend
* **Sistema de Login Seguro:** Autenticación de usuarios con hashing de contraseñas (`Werkzeug Security`).
* **Protección de Rutas:** Decoradores personalizados `@login_required` para restringir accesos no autorizados.
* **API REST:** Endpoints JSON para la comunicación asíncrona entre cliente y servidor.
* **Arquitectura MVC:** Separación lógica de Base de Datos, Lógica y Vistas.

### 🎨 Frontend & UI
* **Diseño Minimalista:** Interfaz limpia inspirada en el ecosistema Apple.
* **Responsive Design:** Adaptable a dispositivos móviles y escritorio.
* **AJAX/Fetch:** Actualización de inventario en tiempo real sin recargar la página.

## 🛠️ Instalación y Configuración

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/SAMUELMARTINEZ8/TechInventory-System.git
    cd TechInventory-System
    ```

2.  **Configurar Entorno Virtual:**
    ```bash
    python -m venv .venv
    # En Windows:
    .venv\Scripts\activate
    ```

3.  **Instalar Dependencias:**
    ```bash
    pip install flask mysql-connector-python
    ```

4.  **Base de Datos:**
    * Crea una base de datos en MySQL llamada `db.sql` (o ajusta `app.py`).
    * Importa las tablas ejecutando los comandos SQL para `productos` y `usuarios`.

5.  **Crear Primer Administrador:**
    * Descomenta temporalmente la ruta `/crear-admin` en `app.py`.
    * Ejecuta el servidor y visita `http://localhost:5000/crear-admin`.
    * Vuelve a proteger la ruta comentando el código.

6.  **Ejecutar:**
    ```bash
    python app.py
    ```

## 📸 Capturas de Pantalla
*(Aquí puedes agregar las imágenes de tu proyecto más adelante)*

---
*Desarrollado por Samuel Martinez* 🐵