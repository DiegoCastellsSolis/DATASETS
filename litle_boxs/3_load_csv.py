import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Conexión a la base de datos (MySQL o PostgreSQL)
# Cambia estos valores según la base de datos a la que te conectes

# Para MySQL
DATABASE_URI = 'mysql+mysqlconnector://usuario:contraseña@localhost/nombre_base_de_datos'

# Para PostgreSQL
# DATABASE_URI = 'postgresql+psycopg2://usuario:contraseña@localhost/nombre_base_de_datos'

# Crear la conexión a la base de datos
engine = create_engine(DATABASE_URI)

# Función para cargar los datos de los CSV a las tablas
def cargar_datos_csv_a_tablas():
    # Leer los archivos CSV generados anteriormente
    usuarios_df = pd.read_csv('usuarios.csv')
    categorias_df = pd.read_csv('categorias.csv')
    experiencias_df = pd.read_csv('experiencias.csv')
    challenges_df = pd.read_csv('challenges.csv')
    participaciones_df = pd.read_csv('participaciones.csv')

    # Cargar los datos en las tablas correspondientes
    usuarios_df.to_sql('Usuarios', con=engine, if_exists='replace', index=False)
    categorias_df.to_sql('Categorias', con=engine, if_exists='replace', index=False)
    experiencias_df.to_sql('Experiencias', con=engine, if_exists='replace', index=False)
    challenges_df.to_sql('Challenges', con=engine, if_exists='replace', index=False)
    participaciones_df.to_sql('Participaciones', con=engine, if_exists='replace', index=False)

    print("Datos cargados correctamente en la base de datos.")

# Ejecutar la carga de los datos
cargar_datos_csv_a_tablas()
