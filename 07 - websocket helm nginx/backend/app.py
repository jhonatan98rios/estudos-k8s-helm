from flask import Flask
from flask_socketio import SocketIO, send
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return "Backend funcionando!"

# Evento para quando um cliente envia uma mensagem
@socketio.on('message')
def handle_message(msg):
    print(f"Mensagem recebida: {msg}")
    send(msg, broadcast=True)  # Envia a mensagem para todos os clientes conectados

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=3000)