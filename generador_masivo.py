from faker import Faker
from random import randint, choice

# Configuraciones
NUM_CLIENTES = 500
CUENTAS_POR_CLIENTE = (1, 3)
TRANSACCIONES_POR_CUENTA = (5, 20)
PORCENTAJE_CON_PRESTAMO = 0.7  # Aumentado al 70%
NUM_ADMINISTRADORES = 10

fake = Faker()

with open("insert_masivo_banco.sql", "w", encoding="utf-8") as f:

    # CLIENTES
    f.write("-- CLIENTES\n")
    for i in range(1, NUM_CLIENTES + 1):
        nombre = fake.first_name()
        apellido = fake.last_name()
        dni = str(randint(10000000, 99999999))
        direccion = fake.address().replace("\n", ", ").replace("'", "''")
        telefono = '9' + str(randint(10000000, 99999999))
        correo = fake.email()
        f.write(f"INSERT INTO CLIENTES (id_cliente, nombre, apellido, dni, direccion, telefono, correo) "
                f"VALUES ({i}, '{nombre}', '{apellido}', '{dni}', '{direccion}', '{telefono}', '{correo}');\n")

    # CUENTAS
    cuenta_id = 1
    f.write("\n-- CUENTAS\n")
    for cliente_id in range(1, NUM_CLIENTES + 1):
        num_cuentas = randint(*CUENTAS_POR_CLIENTE)
        for _ in range(num_cuentas):
            tipo = choice(['Ahorros', 'Corriente'])
            saldo = round(randint(100, 10000) + randint(0, 99)/100, 2)
            fecha = fake.date_between(start_date='-2y', end_date='today')
            f.write(f"INSERT INTO CUENTAS (id_cuenta, tipo_cuenta, saldo, fecha_apertura, id_cliente) "
                    f"VALUES ({cuenta_id}, '{tipo}', {saldo}, '{fecha}', {cliente_id});\n")
            cuenta_id += 1

    # TRANSACCIONES
    transaccion_id = 1
    f.write("\n-- TRANSACCIONES\n")
    for origen_id in range(1, cuenta_id):
        num_trans = randint(*TRANSACCIONES_POR_CUENTA)
        for _ in range(num_trans):
            tipo = choice(['Depósito', 'Retiro', 'Transferencia'])
            monto = round(randint(10, 1000) + randint(0, 99)/100, 2)
            fecha = fake.date_between(start_date='-2y', end_date='today')
            destino_id = origen_id if tipo != 'Transferencia' else randint(1, cuenta_id - 1)
            f.write(f"INSERT INTO TRANSACCIONES (id_transaccion, tipo, monto, fecha, id_cuenta_origen, id_cuenta_destino) "
                    f"VALUES ({transaccion_id}, '{tipo}', {monto}, '{fecha}', {origen_id}, {destino_id});\n")
            transaccion_id += 1

    # ADMINISTRADORES
    f.write("\n-- ADMINISTRADORES\n")
    for admin_id in range(1, NUM_ADMINISTRADORES + 1):
        nombre = fake.name().replace("'", "''")
        usuario = f"admin{admin_id}"
        contraseña = fake.password(length=10)
        f.write(f"INSERT INTO ADMINISTRADORES (id_admin, nombre, usuario, contraseña) "
                f"VALUES ({admin_id}, '{nombre}', '{usuario}', '{contraseña}');\n")

    # PRESTAMOS
    f.write("\n-- PRESTAMOS\n")
    prestamo_id = 1
    clientes_con_prestamo = [i for i in range(1, NUM_CLIENTES + 1) if randint(1, 100) <= PORCENTAJE_CON_PRESTAMO * 100]
    for cliente_id in clientes_con_prestamo:
        monto = round(randint(1000, 10000) + randint(0, 99)/100, 2)
        fecha_aprob = fake.date_between(start_date='-2y', end_date='today')
        tasa = round(randint(5, 15) + randint(0, 99)/100, 2)
        f.write(f"INSERT INTO PRESTAMOS (id_prestamo, monto, fecha_aprobacion, tasa_interes, id_cliente) "
                f"VALUES ({prestamo_id}, {monto}, '{fecha_aprob}', {tasa}, {cliente_id});\n")

        # GESTIÓN DEL PRÉSTAMO
        admin_id = randint(1, NUM_ADMINISTRADORES)
        observaciones = fake.sentence().replace("'", "''")
        f.write(f"INSERT INTO GESTION_PRESTAMOS (id, id_prestamo, id_admin, observaciones) "
                f"VALUES ({prestamo_id}, {prestamo_id}, {admin_id}, '{observaciones}');\n")

        prestamo_id += 1

print("✅ Script SQL 'insert_masivo_banco.sql' generado con 70% de clientes con préstamo.")