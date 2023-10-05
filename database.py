import psycopg2 as bd

conexion = bd.connect(
    user= 'chiperos',
    password = 'chiperos123@',
    host='34.95.227.165',
    port='5432',
    database = 'vacunarg'
)
