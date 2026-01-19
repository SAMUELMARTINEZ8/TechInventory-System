/* PROYECTO: TechInventory Pro
   DESCRIPCIÓN: Script para crear la estructura de la base de datos
   VERSION: 1.0 Final
*/

-- 1. Crear la Base de Datos (si no existe)
CREATE DATABASE IF NOT EXISTS tech_inventory;
USE tech_inventory;

-- 2. Tabla de Usuarios (Administradores)
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    fecha_registro DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 3. Tabla de Productos (Inventario)
CREATE TABLE IF NOT EXISTS productos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    categoria VARCHAR(50),
    precio DECIMAL(10, 2),
    stock INT
);

-- Final Version 1.0