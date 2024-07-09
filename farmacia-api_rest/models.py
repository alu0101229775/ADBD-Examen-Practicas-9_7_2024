###############################################################################
#########         GERARD ANTONY CARAMAZZA VILÁ (45983867J)            #########
#########                 EXAMEN ADBD 09/07/2024                      #########
###############################################################################

# Operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre la base de datos PostgreSQL.

from database import get_db_connection

# Funciones CRUD para la tabla Laboratorio
def get_all_laboratorios():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Laboratorio")
    laboratorios = cursor.fetchall()
    cursor.close()
    conn.close()
    return laboratorios

def get_laboratorio(codigo_laboratorio):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Laboratorio WHERE CodigoLaboratorio = %s", (codigo_laboratorio,))
    laboratorio = cursor.fetchone()
    cursor.close()
    conn.close()
    return laboratorio

def create_laboratorio(laboratorio):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Laboratorio (CodigoLaboratorio, Nombre, Telefono, Direccion, Fax, PersonaDeContacto) VALUES (%s, %s, %s, %s, %s, %s)",
        (laboratorio['CodigoLaboratorio'], laboratorio['Nombre'], laboratorio['Telefono'], laboratorio['Direccion'], laboratorio['Fax'], laboratorio['PersonaDeContacto'])
    )
    conn.commit()
    cursor.close()
    conn.close()

def update_laboratorio(codigo_laboratorio, laboratorio):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Laboratorio SET Nombre = %s, Telefono = %s, Direccion = %s, Fax = %s, PersonaDeContacto = %s WHERE CodigoLaboratorio = %s",
        (laboratorio['Nombre'], laboratorio['Telefono'], laboratorio['Direccion'], laboratorio['Fax'], laboratorio['PersonaDeContacto'], codigo_laboratorio)
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete_laboratorio(codigo_laboratorio):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Laboratorio WHERE CodigoLaboratorio = %s", (codigo_laboratorio,))
    conn.commit()
    cursor.close()
    conn.close()

# Funciones CRUD para la tabla Familia
def get_all_familias():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Familia")
    familias = cursor.fetchall()
    cursor.close()
    conn.close()
    return familias

def get_familia(codigo_familia):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Familia WHERE CodigoFamilia = %s", (codigo_familia,))
    familia = cursor.fetchone()
    cursor.close()
    conn.close()
    return familia

def create_familia(familia):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Familia (CodigoFamilia, Nombre) VALUES (%s, %s)",
        (familia['CodigoFamilia'], familia['Nombre'])
    )
    conn.commit()
    cursor.close()
    conn.close()

def update_familia(codigo_familia, familia):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Familia SET Nombre = %s WHERE CodigoFamilia = %s",
        (familia['Nombre'], codigo_familia)
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete_familia(codigo_familia):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Familia WHERE CodigoFamilia = %s", (codigo_familia,))
    conn.commit()
    cursor.close()
    conn.close()

# Funciones CRUD para la tabla Cliente
def get_all_clientes():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Cliente")
    clientes = cursor.fetchall()
    cursor.close()
    conn.close()
    return clientes

def get_cliente(codigo_cliente):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Cliente WHERE CodigoCliente = %s", (codigo_cliente,))
    cliente = cursor.fetchone()
    cursor.close()
    conn.close()
    return cliente

def create_cliente(cliente):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Cliente (CodigoCliente, Nombre, Direccion, Telefono, Email) VALUES (%s, %s, %s, %s, %s)",
        (cliente['CodigoCliente'], cliente['Nombre'], cliente['Direccion'], cliente['Telefono'], cliente['Email'])
    )
    conn.commit()
    cursor.close()
    conn.close()

def update_cliente(codigo_cliente, cliente):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Cliente SET Nombre = %s, Direccion = %s, Telefono = %s, Email = %s WHERE CodigoCliente = %s",
        (cliente['Nombre'], cliente['Direccion'], cliente['Telefono'], cliente['Email'], codigo_cliente)
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete_cliente(codigo_cliente):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Cliente WHERE CodigoCliente = %s", (codigo_cliente,))
    conn.commit()
    cursor.close()
    conn.close()

# Funciones CRUD para la tabla ClienteConCredito
def get_all_clientes_con_credito():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM ClienteConCredito")
    clientes_con_credito = cursor.fetchall()
    cursor.close()
    conn.close()
    return clientes_con_credito

def get_cliente_con_credito(codigo_cliente):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM ClienteConCredito WHERE CodigoCliente = %s", (codigo_cliente,))
    cliente_con_credito = cursor.fetchone()
    cursor.close()
    conn.close()
    return cliente_con_credito

def create_cliente_con_credito(cliente_con_credito):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ClienteConCredito (CodigoCliente, FechaPago) VALUES (%s, %s)",
        (cliente_con_credito['CodigoCliente'], cliente_con_credito['FechaPago'])
    )
    conn.commit()
    cursor.close()
    conn.close()

def update_cliente_con_credito(codigo_cliente, cliente_con_credito):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE ClienteConCredito SET FechaPago = %s WHERE CodigoCliente = %s",
        (cliente_con_credito['FechaPago'], codigo_cliente)
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete_cliente_con_credito(codigo_cliente):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ClienteConCredito WHERE CodigoCliente = %s", (codigo_cliente,))
    conn.commit()
    cursor.close()
    conn.close()

# Funciones CRUD para la tabla ClienteSinCredito
def get_all_clientes_sin_credito():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM ClienteSinCredito")
    clientes_sin_credito = cursor.fetchall()
    cursor.close()
    conn.close()
    return clientes_sin_credito

def get_cliente_sin_credito(codigo_cliente):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM ClienteSinCredito WHERE CodigoCliente = %s", (codigo_cliente,))
    cliente_sin_credito = cursor.fetchone()
    cursor.close()
    conn.close()
    return cliente_sin_credito

def create_cliente_sin_credito(cliente_sin_credito):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO ClienteSinCredito (CodigoCliente) VALUES (%s)",
        (cliente_sin_credito['CodigoCliente'],)
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete_cliente_sin_credito(codigo_cliente):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ClienteSinCredito WHERE CodigoCliente = %s", (codigo_cliente,))
    conn.commit()
    cursor.close()
    conn.close()

# Funciones CRUD para la tabla DatosBancarios
def get_all_datos_bancarios():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM DatosBancarios")
    datos_bancarios = cursor.fetchall()
    cursor.close()
    conn.close()
    return datos_bancarios

def get_datos_bancarios(codigo_datos_bancarios):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM DatosBancarios WHERE CodigoDatosBancarios = %s", (codigo_datos_bancarios,))
    datos_bancarios = cursor.fetchone()
    cursor.close()
    conn.close()
    return datos_bancarios

def create_datos_bancarios(datos_bancarios):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO DatosBancarios (CodigoCliente, NombreBanco, NumeroCuenta, TipoCuenta) VALUES (%s, %s, %s, %s)",
        (datos_bancarios['CodigoCliente'], datos_bancarios['NombreBanco'], datos_bancarios['NumeroCuenta'], datos_bancarios['TipoCuenta'])
    )
    conn.commit()
    cursor.close()
    conn.close()

def update_datos_bancarios(codigo_datos_bancarios, datos_bancarios):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE DatosBancarios SET NombreBanco = %s, NumeroCuenta = %s, TipoCuenta = %s WHERE CodigoDatosBancarios = %s",
        (datos_bancarios['NombreBanco'], datos_bancarios['NumeroCuenta'], datos_bancarios['TipoCuenta'], codigo_datos_bancarios)
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete_datos_bancarios(codigo_datos_bancarios):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM DatosBancarios WHERE CodigoDatosBancarios = %s", (codigo_datos_bancarios,))
    conn.commit()
    cursor.close()
    conn.close()

# Funciones CRUD para la tabla Medicamento
def get_all_medicamentos():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Medicamento")
    medicamentos = cursor.fetchall()
    cursor.close()
    conn.close()
    return medicamentos

def get_medicamento(codigo_medicamento):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Medicamento WHERE CodigoMedicamento = %s", (codigo_medicamento,))
    medicamento = cursor.fetchone()
    cursor.close()
    conn.close()
    return medicamento

def create_medicamento(medicamento):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Medicamento (CodigoMedicamento, Nombre, Tipo, UnidadesEnStock, UnidadesVendidas, Precio, PrecioVenta, PorcentajeImpuesto, VentaConReceta, CodigoFamilia, CodigoLaboratorio) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (medicamento['CodigoMedicamento'], medicamento['Nombre'], medicamento['Tipo'], medicamento['UnidadesEnStock'], medicamento['UnidadesVendidas'], medicamento['Precio'], medicamento['PrecioVenta'], medicamento['PorcentajeImpuesto'], medicamento['VentaConReceta'], medicamento['CodigoFamilia'], medicamento['CodigoLaboratorio'])
    )
    conn.commit()
    cursor.close()
    conn.close()

def update_medicamento(codigo_medicamento, medicamento):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Medicamento SET Nombre = %s, Tipo = %s, UnidadesEnStock = %s, UnidadesVendidas = %s, Precio = %s, PrecioVenta = %s, PorcentajeImpuesto = %s, VentaConReceta = %s, CodigoFamilia = %s, CodigoLaboratorio = %s WHERE CodigoMedicamento = %s",
        (medicamento['Nombre'], medicamento['Tipo'], medicamento['UnidadesEnStock'], medicamento['UnidadesVendidas'], medicamento['Precio'], medicamento['PrecioVenta'], medicamento['PorcentajeImpuesto'], medicamento['VentaConReceta'], medicamento['CodigoFamilia'], medicamento['CodigoLaboratorio'], codigo_medicamento)
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete_medicamento(codigo_medicamento):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Medicamento WHERE CodigoMedicamento = %s", (codigo_medicamento,))
    conn.commit()
    cursor.close()
    conn.close()

# Funciones CRUD para la tabla Venta
def get_all_ventas():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Venta")
    ventas = cursor.fetchall()
    cursor.close()
    conn.close()
    return ventas

def get_venta(codigo_venta):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Venta WHERE CodigoVenta = %s", (codigo_venta,))
    venta = cursor.fetchone()
    cursor.close()
    conn.close()
    return venta

def create_venta(venta):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Venta (FechaVenta, UnidadesCompradas, CodigoCliente, CodigoMedicamento) VALUES (%s, %s, %s, %s)",
        (venta['FechaVenta'], venta['UnidadesCompradas'], venta['CodigoCliente'], venta['CodigoMedicamento'])
    )
    conn.commit()
    cursor.close()
    conn.close()

def update_venta(codigo_venta, venta):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Venta SET FechaVenta = %s, UnidadesCompradas = %s, CodigoCliente = %s, CodigoMedicamento = %s WHERE CodigoVenta = %s",
        (venta['FechaVenta'], venta['UnidadesCompradas'], venta['CodigoCliente'], venta['CodigoMedicamento'], codigo_venta)
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete_venta(codigo_venta):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Venta WHERE CodigoVenta = %s", (codigo_venta,))
    conn.commit()
    cursor.close()
    conn.close()

# Funciones CRUD para la tabla Pago
def get_all_pagos():
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Pago")
    pagos = cursor.fetchall()
    cursor.close()
    conn.close()
    return pagos

def get_pago(codigo_pago):
    conn = get_db_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM Pago WHERE CodigoPago = %s", (codigo_pago,))
    pago = cursor.fetchone()
    cursor.close()
    conn.close()
    return pago

def create_pago(pago):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Pago (FechaPago, Monto, CodigoVenta) VALUES (%s, %s, %s)",
        (pago['FechaPago'], pago['Monto'], pago['CodigoVenta'])
    )
    conn.commit()
    cursor.close()
    conn.close()

def update_pago(codigo_pago, pago):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Pago SET FechaPago = %s, Monto = %s, CodigoVenta = %s WHERE CodigoPago = %s",
        (pago['FechaPago'], pago['Monto'], pago['CodigoVenta'], codigo_pago)
    )
    conn.commit()
    cursor.close()
    conn.close()

def delete_pago(codigo_pago):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Pago WHERE CodigoPago = %s", (codigo_pago,))
    conn.commit()
    cursor.close()
    conn.close()
