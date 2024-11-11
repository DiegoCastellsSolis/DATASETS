COPY Empresas (id_empresa, nombre, ubicacion, sector, anio_fundacion)
FROM 'ruta/al/archivo/empresas.csv'
DELIMITER ','
CSV HEADER;

COPY Marcas (id_marca, nombre_marca, id_empresa, descripcion)
FROM 'ruta/al/archivo/marcas.csv'
DELIMITER ','
CSV HEADER;

COPY Productos (id_producto, nombre_producto, id_marca, categoria, precio, anio_lanzamiento)
FROM 'ruta/al/archivo/productos.csv'
DELIMITER ','
CSV HEADER;

COPY Ventas (id_venta, id_producto, fecha_venta, cantidad, total_venta)
FROM 'ruta/al/archivo/ventas.csv'
DELIMITER ','
CSV HEADER;
