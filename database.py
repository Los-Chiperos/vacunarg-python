import psycopg2
import time

while True:
    try:
        conexion = psycopg2.connect(
            user='chiperos',
            password='vacunarg123.',
            host='db',
            port='5432',
            database='vacunatorio'
        )
        # Si llegamos a este punto, la conexión fue exitosa, por lo que salimos del ciclo
        break
    except psycopg2.OperationalError as e:
        print('Waiting for connecting to PostgreSQL...')
        # Esperamos un poco antes de volver a intentarlo
        time.sleep(1)
