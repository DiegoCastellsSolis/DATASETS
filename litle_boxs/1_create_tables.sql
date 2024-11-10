CREATE TABLE Usuarios (
    id_usuario INT PRIMARY KEY,
    nombre VARCHAR(100),
    correo VARCHAR(100),
    fecha_registro DATE
);



CREATE TABLE Categorias (
    id_categoria INT PRIMARY KEY,
    nombre_categoria VARCHAR(50)
);


CREATE TABLE Experiencias (
    id_experiencia INT PRIMARY KEY,
    nombre_experiencia VARCHAR(100),
    descripcion TEXT,
    id_categoria INT,
    precio DECIMAL(10, 2),
    fecha_disponibilidad DATE,
    FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria)
);


CREATE TABLE Challenges (
    id_challenge INT PRIMARY KEY,
    nombre_challenge VARCHAR(100),
    descripcion TEXT,
    fecha_inicio DATE,
    fecha_fin DATE
);


CREATE TABLE Participaciones (
    id_participacion INT PRIMARY KEY,
    id_usuario INT,
    id_challenge INT,
    estado VARCHAR(50),  -- Ejemplo: 'en progreso', 'completado'
    fecha_inicio DATE,
    fecha_completado DATE,
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_challenge) REFERENCES Challenges(id_challenge)
);
