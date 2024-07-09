-------------------------------------------------------------------------------
---------         GERARD ANTONY CARAMAZZA VILÁ (45983867J)            ---------
---------                 EXAMEN ADBD 09/07/2024                      ---------
-------------------------------------------------------------------------------

-------------------------------------------------------------------------------
---------                        EJERCICIO 2                          ---------
-------------------------------------------------------------------------------
-- Crear la base de datos
CREATE DATABASE farmacia;
USE farmacia;

-- Crear tablas

-- Tabla Laboratorio
CREATE TABLE Laboratorio (
    CodigoLaboratorio INT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Telefono VARCHAR(20),
    Direccion VARCHAR(255),
    Fax VARCHAR(20),
    PersonaDeContacto VARCHAR(100)
);

-- Tabla Familia
CREATE TABLE Familia (
    CodigoFamilia INT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL
);

-- Tabla Cliente (entidad general)
CREATE TABLE Cliente (
    CodigoCliente INT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Direccion VARCHAR(255),
    Telefono VARCHAR(20),
    Email VARCHAR(100)
);

-- Tabla ClienteConCredito (entidad específica)
CREATE TABLE ClienteConCredito (
    CodigoCliente INT PRIMARY KEY,
    FOREIGN KEY (CodigoCliente) REFERENCES Cliente(CodigoCliente),
    FechaPago DATE
);

-- Tabla ClienteSinCredito (entidad específica)
CREATE TABLE ClienteSinCredito (
    CodigoCliente INT PRIMARY KEY,
    FOREIGN KEY (CodigoCliente) REFERENCES Cliente(CodigoCliente)
);

-- Tabla DatosBancarios (entidad débil)
CREATE TABLE DatosBancarios (
    CodigoDatosBancarios INT PRIMARY KEY AUTO_INCREMENT,
    CodigoCliente INT,
    NombreBanco VARCHAR(100),
    NumeroCuenta VARCHAR(20),
    TipoCuenta VARCHAR(50),
    FOREIGN KEY (CodigoCliente) REFERENCES ClienteConCredito(CodigoCliente)
);

-- Tabla Medicamento
CREATE TABLE Medicamento (
    CodigoMedicamento INT PRIMARY KEY,
    Nombre VARCHAR(100) NOT NULL,
    Tipo VARCHAR(50),
    UnidadesEnStock INT,
    UnidadesVendidas INT,
    Precio DECIMAL(10, 2),
    PrecioVenta DECIMAL(10, 2),
    PorcentajeImpuesto DECIMAL(5, 2),
    VentaConReceta BOOLEAN,
    CodigoFamilia INT,
    CodigoLaboratorio INT,
    FOREIGN KEY (CodigoFamilia) REFERENCES Familia(CodigoFamilia),
    FOREIGN KEY (CodigoLaboratorio) REFERENCES Laboratorio(CodigoLaboratorio)
);

-- Tabla Venta
CREATE TABLE Venta (
    CodigoVenta INT PRIMARY KEY AUTO_INCREMENT,
    FechaVenta DATE,
    UnidadesCompradas INT,
    CodigoCliente INT,
    CodigoMedicamento INT,
    FOREIGN KEY (CodigoCliente) REFERENCES Cliente(CodigoCliente),
    FOREIGN KEY (CodigoMedicamento) REFERENCES Medicamento(CodigoMedicamento)
);

-- Tabla Pago (entidad débil)
CREATE TABLE Pago (
    CodigoPago INT PRIMARY KEY AUTO_INCREMENT,
    FechaPago DATE,
    Monto DECIMAL(10, 2),
    CodigoVenta INT,
    FOREIGN KEY (CodigoVenta) REFERENCES Venta(CodigoVenta)
);

-- Insertar datos en las tablas

-- Insertar datos en Laboratorio
INSERT INTO Laboratorio (CodigoLaboratorio, Nombre, Telefono, Direccion, Fax, PersonaDeContacto) VALUES
(1, 'Laboratorio A', '123456789', 'Direccion A', '987654321', 'Contacto A'),
(2, 'Laboratorio B', '223456789', 'Direccion B', '887654321', 'Contacto B'),
(3, 'Laboratorio C', '323456789', 'Direccion C', '787654321', 'Contacto C'),
(4, 'Laboratorio D', '423456789', 'Direccion D', '687654321', 'Contacto D'),
(5, 'Laboratorio E', '523456789', 'Direccion E', '587654321', 'Contacto E');

-- Insertar datos en Familia
INSERT INTO Familia (CodigoFamilia, Nombre) VALUES
(1, 'Antibióticos'),
(2, 'Analgésicos'),
(3, 'Antihistamínicos'),
(4, 'Antiinflamatorios'),
(5, 'Antipiréticos');

-- Insertar datos en Cliente
INSERT INTO Cliente (CodigoCliente, Nombre, Direccion, Telefono, Email) VALUES
(1, 'Cliente 1', 'Direccion 1', '123456789', 'cliente1@example.com'),
(2, 'Cliente 2', 'Direccion 2', '223456789', 'cliente2@example.com'),
(3, 'Cliente 3', 'Direccion 3', '323456789', 'cliente3@example.com'),
(4, 'Cliente 4', 'Direccion 4', '423456789', 'cliente4@example.com'),
(5, 'Cliente 5', 'Direccion 5', '523456789', 'cliente5@example.com');

-- Insertar datos en ClienteConCredito
INSERT INTO ClienteConCredito (CodigoCliente, FechaPago) VALUES
(1, '2024-07-01'),
(3, '2024-07-01'),
(5, '2024-07-01');

-- Insertar datos en ClienteSinCredito
INSERT INTO ClienteSinCredito (CodigoCliente) VALUES
(2),
(4);

-- Insertar datos en DatosBancarios
INSERT INTO DatosBancarios (CodigoCliente, NombreBanco, NumeroCuenta, TipoCuenta) VALUES
(1, 'Banco A', '111111', 'Corriente'),
(3, 'Banco B', '222222', 'Ahorro'),
(5, 'Banco C', '333333', 'Corriente');

-- Insertar datos en Medicamento
INSERT INTO Medicamento (CodigoMedicamento, Nombre, Tipo, UnidadesEnStock, UnidadesVendidas, Precio, PrecioVenta, PorcentajeImpuesto, VentaConReceta, CodigoFamilia, CodigoLaboratorio) VALUES
(1, 'Medicamento A', 'Jarabe', 100, 10, 5.00, 6.00, 10.00, TRUE, 1, 1),
(2, 'Medicamento B', 'Comprimido', 200, 20, 10.00, 12.00, 10.00, FALSE, 2, 2),
(3, 'Medicamento C', 'Pomada', 150, 15, 7.00, 8.50, 10.00, TRUE, 3, 3),
(4, 'Medicamento D', 'Jarabe', 120, 12, 6.00, 7.50, 10.00, FALSE, 4, 4),
(5, 'Medicamento E', 'Comprimido', 80, 8, 9.00, 10.50, 10.00, TRUE, 5, 5);

-- Insertar datos en Venta
INSERT INTO Venta (FechaVenta, UnidadesCompradas, CodigoCliente, CodigoMedicamento) VALUES
('2024-07-01', 5, 1, 1),
('2024-07-02', 10, 2, 2),
('2024-07-03', 7, 3, 3),
('2024-07-04', 8, 4, 4),
('2024-07-05', 6, 5, 5);

-- Insertar datos en Pago
INSERT INTO Pago (FechaPago, Monto, CodigoVenta) VALUES
('2024-07-10', 30.00, 1),
('2024-07-11', 120.00, 2),
('2024-07-12', 49.00, 3),
('2024-07-13', 60.00, 4),
('2024-07-14', 63.00, 5);

-------------------------------------------------------------------------------
---------                        EJERCICIO 3                          ---------
-------------------------------------------------------------------------------
-- Crear trigger
-- Este trigger se activa después de una inserción en la tabla Compra.
-- Actualiza las unidades en stock y unidades vendidas en la tabla Medicamento.
DELIMITER //
CREATE TRIGGER ActualizarStockYVentasDespuesDeCompra
AFTER INSERT ON Compra
FOR EACH ROW
BEGIN
    UPDATE Medicamento
    SET UnidadesEnStock = UnidadesEnStock - NEW.UnidadesCompradas,
        UnidadesVendidas = UnidadesVendidas + NEW.UnidadesCompradas
    WHERE CodigoMedicamento = NEW.CodigoMedicamento;
END;
//
DELIMITER ;