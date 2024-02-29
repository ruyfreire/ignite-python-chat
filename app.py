from flask import Flask, send_file
from flask_socketio import SocketIO, send
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
socketio = SocketIO(app)

@app.route('/', methods=['GET'])
def home():
    return send_file('templates/index.html')

@socketio.on('connect')
def on_connect():
    print('Client connected')

@socketio.on('message')
def handle_message(message):
    send(message, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)