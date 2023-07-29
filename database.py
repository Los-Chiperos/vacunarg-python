import psycopg2 as bd

conexion = bd.connect(
    user= 'chiperos',
    password = 'vacunarg123.',
    host='172.18.0.2',
    port='5432',
    database = 'vacunatorio'
)
