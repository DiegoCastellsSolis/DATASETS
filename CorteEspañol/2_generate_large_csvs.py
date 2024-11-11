import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

# Inicializar Faker
fake = Faker()

# Función para generar datos de empresas
def generar_empresas(num_registros=100):
    datos = []
    for i in range(1, num_registros + 1):
        datos.append([i, fake.company(), fake.country(), random.choice(['Electrónica', 'Electrodomésticos', 'Tecnología']), random.randint(1950, 2023)])
    return pd.DataFrame(datos, columns=['id_empresa', 'nombre', 'ubicacion', 'sector', 'anio_fundacion'])

# Función para generar datos de marcas
def generar_marcas(num_registros=500, max_empresas=100):
    datos = []
    for i in range(1, num_registros + 1):
        id_empresa = random.randint(1, max_empresas)
        datos.append([i, fake.company_suffix(), id_empresa, fake.catch_phrase()])
    return pd.DataFrame(datos, columns=['id_marca', 'nombre_marca', 'id_empresa', 'descripcion'])

# Función para generar datos de productos
def generar_productos(num_registros=10000, max_marcas=500):
    categorias = ['Televisión', 'Climatización', 'Tecnología', 'Electrodomésticos', 'Audio']
    datos = []
    for i in range(1, num_registros + 1):
        id_marca = random.randint(1, max_marcas)
        datos.append([i, fake.word().capitalize() + ' ' + random.choice(categorias), id_marca, random.choice(categorias), round(random.uniform(1000, 150000), 2), random.randint(2000, 2024)])
    return pd.DataFrame(datos, columns=['id_producto', 'nombre_producto', 'id_marca', 'categoria', 'precio', 'anio_lanzamiento'])

# Función para generar datos de ventas
def generar_ventas(num_registros=100000, max_productos=10000):
    datos = []
    for i in range(1, num_registros + 1):
        id_producto = random.randint(1, max_productos)
        fecha_venta = datetime.now() - timedelta(days=random.randint(0, 365 * 5))
        cantidad = random.randint(1, 500)
        precio_unitario = round(random.uniform(1000, 150000), 2)  # Simular precio
        total_venta = round(precio_unitario * cantidad, 2)
        datos.append([i, id_producto, fecha_venta.strftime('%Y-%m-%d'), cantidad, total_venta])
    return pd.DataFrame(datos, columns=['id_venta', 'id_producto', 'fecha_venta', 'cantidad', 'total_venta'])

# Generar los datasets y guardarlos en CSV
empresas_df = generar_empresas()
marcas_df = generar_marcas(max_empresas=100)
productos_df = generar_productos(max_marcas=500)
ventas_df = generar_ventas(max_productos=10000)

# Guardar en archivos CSV
empresas_df.to_csv('empresas.csv', index=False)
marcas_df.to_csv('marcas.csv', index=False)
productos_df.to_csv('productos.csv', index=False)
ventas_df.to_csv('ventas.csv', index=False)

print("Archivos CSV generados exitosamente.")
                                                                                                                                                                                                                                                                                                                                                                                            