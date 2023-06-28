from flask import Flask, jsonify, request, session, url_for, render_template
from flask_cors import CORS
from database import conexion as db
from api import home, agregar_paciente, borrar_paciente, editar_paciente, buscar_paciente
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
from login import login

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["https://app.vacunarg.site"]}})
app.secret_key = 'clave_secreta'  # Cambia esto por una clave secreta más segura
app.config['JWT_SECRET_KEY'] = 'clave_secreta_jwt'  # Cambia esto por una clave secreta para JWT
jwt = JWTManager(app)

# Rutas

# Home
app.route('/')(home)

# Agregar Paciente
app.route('/agregar_paciente', methods=['POST'])(agregar_paciente)

#Borrar paciente
app.route('/borrar_paciente/<int:id>', methods=['DELETE'])(borrar_paciente)

#Editar paciente
app.route('/editar_paciente/<int:id>', methods=['PUT'])(editar_paciente)

app.route('/buscar_paciente', methods=['POST'])(buscar_paciente)

#Login
app.route('/login', methods=['GET','POST'])(login)


@app.route('/bienvenido')
@jwt_required()
def bienvenido():
    username = get_jwt_identity()
    return f'Hola, {username}! <a href="/logout">Cerrar sesión</a>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
