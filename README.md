🏦 Sistema de Base de Datos para Entidad Financiera

📌 Descripción del Proyecto

Este proyecto consiste en el diseño, modelado y desarrollo de un sistema de base de datos para una entidad financiera ficticia. El sistema está diseñado para gestionar eficientemente la información de clientes, cuentas bancarias, transacciones, préstamos y su respectiva gestión por parte de administradores. El enfoque principal es mantener la integridad de los datos y permitir operaciones básicas y consultas útiles para análisis financiero.

📁 Estructura del Proyecto

Modelamiento ER: Diagrama entidad-relación y modelo relacional.
Script de Creación SQL: Código para crear las 6 tablas relacionales.
Generador de Datos: Script en Python que usa Faker para insertar datos masivos realistas.
Consultas SQL: Conjunto de consultas para validar el modelo y obtener reportes clave.
Evidencias: Capturas del trabajo realizado en equipo y resultados de ejecución.

🧩 Entidades Principales

Tabla	Descripción

CLIENTES	Información de usuarios registrados en la entidad financiera.
CUENTAS	Registra las cuentas bancarias de los clientes (ahorros, corriente).
TRANSACCIONES	Movimientos realizados por los clientes (depósitos, retiros, transferencias).
PRESTAMOS	Créditos otorgados a los clientes, con tasa e historial.
ADMINISTRADORES	Personal responsable de autorizar y gestionar préstamos.
GESTION_PRESTAMOS	Relación entre préstamos y administradores con observaciones.

⚙ Tecnologías Utilizadas

SQL Server – Gestión del sistema de base de datos.
Python 3 – Generación masiva de datos ficticios.
Faker – Librería para simular datos realistas.
Visual Studio Code / SSMS – Herramientas para desarrollo y pruebas.

🚀 Objetivos del Sistema

Centralizar la gestión de clientes, cuentas y préstamos.
Asegurar la integridad relacional mediante claves primarias y foráneas.
Simular escenarios reales de una entidad financiera para pruebas y aprendizaje.
Facilitar reportes y consultas de interés administrativo y contable.

Proyecto realizado durante el curso SQL Server / Idat
     -Docente: Jose Montenegro - Desarrollador full stack
👥 Integrantes del Proyecto
Jorge Yataco Torres – Desarrollador SQL
John Fernandez Mora – Analista de Requisitos
Mauricio – Diseñador del Modelo ER
Pamela Llacsa Aguilar – Responsable de Evidencias
Marcello Nonato Vertiz – Documentador

-Docente: Jose Montenegro

💾 Archivo Generador
> El script `generador_banco.py` crea un archivo SQL con más de 10,000 registros usando Faker para poblar la base de datos.
