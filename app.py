from flask import Flask, jsonify, request
import os
from database import conexion as db

app = Flask(__name__)

@app.route('/')
def home():
    insertObject = []
    try:
        with db: 
            with db.cursor() as cursor:
                sentencia = 'SELECT * FROM paciente'
                cursor.execute(sentencia)
                myresult = cursor.fetchall()
                
                columNames = [column[0] for column in cursor.description]
                for record in myresult:
                    insertObject.append(dict(zip(columNames, record)))

                return jsonify(insertObject)
    except Exception as e:
        print(f'Ocurrió un error: {e}')
        return jsonify({"error": str(e)})

@app.route('/agregar_paciente', methods=['POST'])
def agregar_paciente():
    data = request.json
    nombre = data['nombre']
    apellido = data['apellido']
    nro_dni = data['nro_dni']
    fecha_nacimiento = data['fecha_nacimiento']
    dosis = data['dosis']
    fecha_aplicacion = data['fecha_aplicacion']
    centro_salud = data['centro_salud']
    nombre_vacuna = data['nombre_vacuna']
    lote_vacuna = data['lote_vacuna']
    try:
        with db:
            with db.cursor() as cursor:
                sentencia = 'INSERT INTO paciente (nombre,apellido,nro_dni,fecha_nacimiento,dosis,fecha_aplicacion, centro_salud, nombre_vacuna, lote_vacuna) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
                valores = (nombre,apellido,nro_dni,fecha_nacimiento,dosis,
                        fecha_aplicacion, centro_salud, nombre_vacuna, lote_vacuna)
                cursor.execute(sentencia,valores)

                return jsonify({"success": "Paciente agregado correctamente."})
    except Exception as e:
        print(f'Ocurrió un error al cargar los datos: {e}')
        return jsonify({"error": str(e)})

@app.route('/borrar_paciente/<int:id>', methods=['DELETE'])
def borrar_paciente(id):
    try:
        with db:
            with db.cursor() as cursor:
                sentencia = 'DELETE FROM paciente WHERE id_paciente = %s'
                cursor.execute(sentencia, (id,))

                return jsonify({"success": "Paciente eliminado correctamente."})
    except Exception as e:
        print(f'No se puedo borrar el paciente: {e}')
        return jsonify({"error": str(e)})

@app.route('/editar_paciente/<int:id>', methods=['PUT'])
def editar_paciente(id):
    data = jsonify
    nombre = data['nombre']
    apellido = data['apellido']
    nro_dni = data['nro_dni']
    fecha_nacimiento = data['fecha_nacimiento']
    dosis = data['dosis']
    centro_salud = data['centro_salud']
    
    try:
        with db:
            with db.cursor() as cursor:
                sentencia = 'UPDATE paciente SET nombre=%s, apellido=%s,nro_dni=%s, fecha_nacimiento=%s, dosis=%s, centro_salud=%s WHERE id_paciente=%s'
                valores = (nombre,apellido,nro_dni,fecha_nacimiento,dosis,
                        centro_salud, id)
                cursor.execute(sentencia, valores)

                return jsonify({"success": "Paciente actualizado correctamente."})
    except Exception as e:
        print(f'No se pudo modificar los valores: {e}')
        return jsonify({"error": str(e)})
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)

