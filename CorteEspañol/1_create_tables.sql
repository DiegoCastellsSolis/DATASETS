CREATE TABLE Empresas (
    id_empresa INT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    ubicacion VARCHAR(50),
    sector VARCHAR(50),
    anio_fundacion INT
);

CREATE TABLE Marcas (
    id_marca INT PRIMARY KEY,
    nombre_marca VARCHAR(50) NOT NULL,
    id_empresa INT,
    descripcion VARCHAR(255),
    FOREIGN KEY (id_empresa) REFERENCES Empresas(id_empresa)
);

CREATE TABLE Productos (
    id_producto INT PRIMARY KEY,
    nombre_producto VARCHAR(50) NOT NULL,
    id_marca INT,
    categoria VARCHAR(50),
    precio DECIMAL(10, 2),
    anio_lanzamiento INT,
    FOREIGN KEY (id_marca) REFERENCES Marcas(id_marca)
);

CREATE TABLE Ventas (
    id_venta INT PRIMARY KEY,
    id_producto INT,
    fecha_venta DATE,
    cantidad INT,
    total_venta DECIMAL(15, 2),
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);
