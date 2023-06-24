import psycopg2 as bd

conexion = bd.connect(
    user= 'chiperos',
    password = 'vacunarg123.',
    host='base-vacunarg.postgres.database.azure.com',
    port='5432',
    database = 'vacunatorio'
)