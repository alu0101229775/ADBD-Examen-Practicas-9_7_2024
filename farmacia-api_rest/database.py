###############################################################################
#########         GERARD ANTONY CARAMAZZA VILÁ (45983867J)            #########
#########                 EXAMEN ADBD 09/07/2024                      #########
###############################################################################

# Gestión de la conexión a la base de datos PostgreSQL.

import psycopg2
from psycopg2.extras import RealDictCursor

def get_db_connection():
    connection = psycopg2.connect(
        host="localhost",
        database="farmacia",
        user="alu0101229775",  # Se debe indicar el usuario para el acceso
        password="password"    # Se debe indicar la contraseña del usuario
    )
    return connection
