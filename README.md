# 📦 TechInventory Pro

> Sistema de Gestión de Inventario Inteligente desarrollado con Python y Flask.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Microframework-000000?style=flat&logo=flask&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=flat&logo=mysql&logoColor=white)
![Status](https://img.shields.io/badge/Estado-Terminado-success)

## 📖 Descripción
**TechInventory Pro** es una aplicación web completa para la administración de productos tecnológicos. Permite a las empresas mantener un control en tiempo real de su stock, gestionar precios y categorías, todo bajo una interfaz minimalista y segura.

## ✨ Características Principales
* **🔐 Autenticación Segura:** Sistema de Login y Registro con encriptación de contraseñas (Hash).
* **📝 CRUD Completo:** Funcionalidades para **C**rear, **L**eer, **E**ditar y **E**liminar productos.
* **🎨 Diseño Minimalista:** Interfaz limpia y moderna (CSS puro) enfocada en la experiencia de usuario (UX).
* **🗄️ Base de Datos SQL:** Estructura relacional optimizada para alto rendimiento.
* **📱 Responsive:** Adaptable a diferentes tamaños de pantalla.

## 🚀 Instalación y Configuración

### 1. Requisitos Previos
* Python 3.x
* XAMPP (para MySQL)
* Git

### 2. Configuración de la Base de Datos
1.  Abre **XAMPP** e inicia los servicios Apache y MySQL.
2.  Entra a **phpMyAdmin**.
3.  Importa el archivo `db.sql` incluido en este repositorio o crea la base de datos `tech_inventory` manualmente.

### 3. Ejecución del Proyecto
```bash
# Instalar dependencias
pip install flask mysql-connector-python werkzeug

# Ejecutar el servidor
python app.py

---
*Desarrollado por Samuel Martinez* 🐵