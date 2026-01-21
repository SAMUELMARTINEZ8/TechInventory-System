# 📦 TechInventory Pro

> Sistema de Gestión de Inventario Inteligente desarrollado con Python y Flask.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Microframework-000000?style=flat&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=flat&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Estado-Terminado-success)
![License](https://img.shields.io/badge/Licencia-MIT-green)

---

## 📖 Descripción

**TechInventory Pro** es una aplicación web completa diseñada para la administración eficiente de productos tecnológicos. Este sistema permite a las empresas y administradores mantener un control en tiempo real de su stock, gestionar precios, categorías y usuarios, todo bajo una interfaz minimalista, moderna y segura.

El proyecto implementa una arquitectura **MVC** (Modelo-Vista-Controlador) utilizando **Flask** como backend y **MySQL** como motor de base de datos.

---

## ✨ Características Principales

### 🛠️ Gestión de Inventario (CRUD Completo)
* **Crear:** Registro de nuevos equipos con categoría, precio y stock.
* **Leer:** Visualización en tiempo real del inventario en una tabla dinámica.
* **Actualizar:** Edición de productos existentes (precios, stock, nombres).
* **Eliminar:** Borrado seguro de productos con confirmación de seguridad.

### 🔐 Seguridad y Usuarios
* **Login Seguro:** Sistema de autenticación de administradores.
* **Registro de Usuarios:** Creación de nuevas cuentas administrativas.
* **Protección de Datos:** Contraseñas encriptadas mediante Hashing (`werkzeug.security`).
* **Control de Sesiones:** Protección de rutas (Middleware) para evitar accesos no autorizados.

### 🎨 Diseño e Interfaz (UI/UX)
* **Estilo Minimalista:** Diseño limpio inspirado en interfaces modernas.
* **Feedback Visual:** Alertas de stock, confirmaciones de eliminación y estados de carga.
* **Responsive:** Adaptable a diferentes resoluciones de pantalla.

---

## 🚀 Instalación y Configuración

Sigue estos pasos para ejecutar el proyecto en tu entorno local.

### 1. Requisitos Previos
Asegúrate de tener instalado:
* [Python 3.x](https://www.python.org/)
* [XAMPP](https://www.apachefriends.org/) (o cualquier servidor MySQL)
* [Git](https://git-scm.com/)

### 2. Clonar el Repositorio
```bash
git clone https://github.com/SAMUELMARTINEZ8/TechInventory-System.git
cd TechInventory-System
```

### 3. Configurar Entorno Virtual
```bash
python -m venv venv
# En Windows:
.\venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate
```

### 4 Instalar Dependencias
```bash
pip install -r requirements.txt
```

### 5. Base de Datos
1. Abre tu gestor de base de datos (phpMyAdmin o Workbench).
2. Importa el archivo db.sql que viene en el proyecto.
3. Configura tus credenciales de MySQL en el archivo app.py.

### 6. Ejecutar la aplicación
```bash
python app.py
```
El sistema estará disponible en: http://localhost:5000/

---
*Desarrollado por Samuel Martinez* 🐵