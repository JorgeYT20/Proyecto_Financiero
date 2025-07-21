create database Proyecto_financiero;
use Proyecto_financiero;

--------------------------------------------------------
-- SCRIPT DE CREACIÓN DE TABLAS PARA SISTEMA BANCARIO--
--------------------------------------------------------
--1. Crear la base de datos
--2. Usar la base de datos
--3. Usar el script para crear las tablas

-- Tabla CLIENTES
CREATE TABLE CLIENTES (
    id_cliente INT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    dni CHAR(8),
    direccion VARCHAR(200),
    telefono CHAR(9),
    correo VARCHAR(100)
);

-- Tabla CUENTAS
CREATE TABLE CUENTAS (
    id_cuenta INT PRIMARY KEY,
    tipo_cuenta VARCHAR(50),
    saldo DECIMAL,
    fecha_apertura DATE,
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES CLIENTES(id_cliente)
);

-- Tabla PRESTAMOS
CREATE TABLE PRESTAMOS (
    id_prestamo INT PRIMARY KEY,
    monto DECIMAL,
    fecha_aprobacion DATE,
    tasa_interes DECIMAL,
    id_cliente INT,
    FOREIGN KEY (id_cliente) REFERENCES CLIENTES(id_cliente)
);

-- Tabla TRANSACCIONES
CREATE TABLE TRANSACCIONES (
    id_transaccion INT PRIMARY KEY,
    tipo VARCHAR(50),
    monto DECIMAL,
    fecha DATE,
    id_cuenta_origen INT,
    id_cuenta_destino INT,
    FOREIGN KEY (id_cuenta_origen) REFERENCES CUENTAS(id_cuenta),
    FOREIGN KEY (id_cuenta_destino) REFERENCES CUENTAS(id_cuenta)
);

-- Tabla ADMINISTRADORES
CREATE TABLE ADMINISTRADORES (
    id_admin INT PRIMARY KEY,
    nombre VARCHAR(100),
    usuario VARCHAR(50),
    contraseña VARCHAR(100)
);

-- Tabla GESTION_PRESTAMOS
CREATE TABLE GESTION_PRESTAMOS (
    id INT PRIMARY KEY,
    id_prestamo INT,
    id_admin INT,
    observaciones TEXT,
    FOREIGN KEY (id_prestamo) REFERENCES PRESTAMOS(id_prestamo),
    FOREIGN KEY (id_admin) REFERENCES ADMINISTRADORES(id_admin)
);