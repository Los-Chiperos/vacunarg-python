import psycopg2 as bd

conexion = bd.connect(
    user= 'chiperos',
    password = 'vacunarg123.',
    host='db',
    port='5432',
    database = 'vacunarg'
)
