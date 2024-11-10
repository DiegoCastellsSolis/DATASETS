-- Cargar datos en la tabla de Usuarios
COPY Usuarios (id_usuario, nombre, correo, fecha_registro)
FROM '/ruta/a/tu/usuarios.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',', QUOTE '"');

-- Cargar datos en la tabla de Categorias
COPY Categorias (id_categoria, nombre_categoria)
FROM '/ruta/a/tu/categorias.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',', QUOTE '"');

-- Cargar datos en la tabla de Experiencias
COPY Experiencias (id_experiencia, nombre_experiencia, descripcion, id_categoria, precio, fecha_disponibilidad)
FROM '/ruta/a/tu/experiencias.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',', QUOTE '"');

-- Cargar datos en la tabla de Challenges
COPY Challenges (id_challenge, nombre_challenge, descripcion, fecha_inicio, fecha_fin)
FROM '/ruta/a/tu/challenges.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',', QUOTE '"');

-- Cargar datos en la tabla de Participaciones
COPY Participaciones (id_participacion, id_usuario, id_challenge, estado, fecha_inicio, fecha_completado)
FROM '/ruta/a/tu/participaciones.csv'
WITH (FORMAT csv, HEADER true, DELIMITER ',', QUOTE '"');
