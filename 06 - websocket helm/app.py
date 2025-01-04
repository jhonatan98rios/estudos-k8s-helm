from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

# Rota para servir a página HTML (um simples frontend de chat)
@app.route('/')
def index():
    return render_template('index.html')

# Evento para quando um cliente envia uma mensagem
@socketio.on('message')
def handle_message(msg):
    print(f"Mensagem recebida: {msg}")
    send(msg, broadcast=True)  # Envia a mensagem para todos os clientes conectados

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)