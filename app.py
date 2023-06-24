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
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    nro_dni = request.form['nro_dni']
    fecha_nacimiento = request.form['fecha_nacimiento']
    dosis = request.form['dosis']
    fecha_aplicacion = request.form['fecha_aplicacion']
    centro_salud = request.form['centro_salud']
    nombre_vacuna = request.form['nombre_vacuna']
    lote_vacuna = request.form['lote_vacuna']
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
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    nro_dni = request.form['nro_dni']
    fecha_nacimiento = request.form['fecha_nacimiento']
    dosis = request.form['dosis']
    centro_salud = request.form['centro_salud']
    
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
    app.run(debug=True, port=5000)
