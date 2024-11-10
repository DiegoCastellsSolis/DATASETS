import random
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta

# Inicializar Faker
fake = Faker()

# Función para generar fechas aleatorias dentro de un rango
def random_date(start_date, end_date):
    return start_date + timedelta(seconds=random.randint(0, int((end_date - start_date).total_seconds())))

# Generar datos para la tabla de Usuarios
def generate_usuarios(num_records):
    usuarios = []
    for _ in range(num_records):
        id_usuario = fake.unique.random_number(digits=5)
        nombre = fake.name()
        correo = fake.email()
        fecha_registro = random_date(datetime(2020, 1, 1), datetime(2024, 11, 1)).date()
        usuarios.append([id_usuario, nombre, correo, fecha_registro])
    return pd.DataFrame(usuarios, columns=["id_usuario", "nombre", "correo", "fecha_registro"])

# Generar datos para la tabla de Categorías
def generate_categorias():
    categorias = ['Aventura', 'Bienestar', 'Gastronomía', 'Cultura', 'Viajes']
    return pd.DataFrame([[i+1, categoria] for i, categoria in enumerate(categorias)], columns=["id_categoria", "nombre_categoria"])

# Generar datos para la tabla de Experiencias
def generate_experiencias(num_records, categorias):
    experiencias = []
    for _ in range(num_records):
        id_experiencia = fake.unique.random_number(digits=5)
        nombre_experiencia = fake.bs().title()
        descripcion = fake.text(max_nb_chars=200)
        id_categoria = random.choice(categorias["id_categoria"].tolist())
        precio = round(random.uniform(20, 300), 2)
        fecha_disponibilidad = random_date(datetime(2024, 1, 1), datetime(2025, 1, 1)).date()
        experiencias.append([id_experiencia, nombre_experiencia, descripcion, id_categoria, precio, fecha_disponibilidad])
    return pd.DataFrame(experiencias, columns=["id_experiencia", "nombre_experiencia", "descripcion", "id_categoria", "precio", "fecha_disponibilidad"])

# Generar datos para la tabla de Challenges
def generate_challenges(num_records):
    challenges = []
    for _ in range(num_records):
        id_challenge = fake.unique.random_number(digits=5)
        nombre_challenge = fake.bs().title()
        descripcion = fake.text(max_nb_chars=200)
        fecha_inicio = random_date(datetime(2024, 1, 1), datetime(2024, 5, 1)).date()
        fecha_fin = random_date(fecha_inicio, datetime(2024, 12, 31)).date()
        challenges.append([id_challenge, nombre_challenge, descripcion, fecha_inicio, fecha_fin])
    return pd.DataFrame(challenges, columns=["id_challenge", "nombre_challenge", "descripcion", "fecha_inicio", "fecha_fin"])

# Generar datos para la tabla de Participaciones
def generate_participaciones(num_records, usuarios, challenges):
    participaciones = []
    for _ in range(num_records):
        id_participacion = fake.unique.random_number(digits=5)
        id_usuario = random.choice(usuarios["id_usuario"].tolist())
        id_challenge = random.choice(challenges["id_challenge"].tolist())
        estado = random.choice(['en progreso', 'completado', 'pendiente'])
        fecha_inicio = random_date(datetime(2024, 1, 1), datetime(2024, 11, 1)).date()
        fecha_completado = None
        if estado == 'completado':
            fecha_completado = random_date(fecha_inicio, datetime(2024, 11, 1)).date()
        participaciones.append([id_participacion, id_usuario, id_challenge, estado, fecha_inicio, fecha_completado])
    return pd.DataFrame(participaciones, columns=["id_participacion", "id_usuario", "id_challenge", "estado", "fecha_inicio", "fecha_completado"])

# Generar todos los datasets
def generate_datasets(num_usuarios, num_experiencias, num_challenges, num_participaciones):
    # Generar Usuarios
    usuarios_df = generate_usuarios(num_usuarios)
    # Generar Categorías
    categorias_df = generate_categorias()
    # Generar Experiencias
    experiencias_df = generate_experiencias(num_experiencias, categorias_df)
    # Generar Challenges
    challenges_df = generate_challenges(num_challenges)
    # Generar Participaciones
    participaciones_df = generate_participaciones(num_participaciones, usuarios_df, challenges_df)
    
    # Guardar los datasets como archivos CSV
    usuarios_df.to_csv('usuarios.csv', index=False)
    categorias_df.to_csv('categorias.csv', index=False)
    experiencias_df.to_csv('experiencias.csv', index=False)
    challenges_df.to_csv('challenges.csv', index=False)
    participaciones_df.to_csv('participaciones.csv', index=False)

# Generar 500 usuarios, 1000 experiencias, 200 challenges y 1500 participaciones
generate_datasets(num_usuarios=500, num_experiencias=1000, num_challenges=200, num_participaciones=1500)
