import psycopg2 as bd

conexion = bd.connect(
    user= 'chiperos',
    password = 'vacunarg123.',
    host='localhost',
    port='5432',
    database = 'vacunatorio'
)
