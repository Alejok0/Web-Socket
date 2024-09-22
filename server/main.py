from flask import Flask, send_from_directory, request
from flask_socketio import SocketIO, emit
import logging
import mysql.connector

# Configurar el logger
logging.basicConfig(level=logging.DEBUG)

# Configurar la base de datos
db_config = {
    'user': 'root',
    'password': '',  # Cambia la contraseña si es necesario
    'host': 'localhost',
    'database': 'sockets'
}

# Crear la conexión a la base de datos
def db_query(query, params=None):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
    conn.close()

# Crear la aplicación Flask y configurar SocketIO
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins='*')

# Manejar las conexiones de socket
@socketio.on('connect')
def handle_connect():
    logging.info('A user connected!')

@socketio.on('disconnect')
def handle_disconnect():
    logging.info('A user has disconnected')

@socketio.on('chat message')
def handle_chat_message(data):
    username = data.get('username', 'Anonimo')
    msg = data.get('message', '')

    logging.info(f'Message: "{msg}" from: {username}')

    # Guardar el mensaje en la base de datos
    db_query('INSERT INTO messages (content, user) VALUES (%s, %s)', (msg, username))

    # Emitir el mensaje a todos los clientes conectados
    emit('chat message', {'user': username, 'message': msg}, broadcast=True)

# Rutas
@app.route('/')
def index():
    return send_from_directory('', 'index.html')

# Iniciar el servidor
if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=2002)
