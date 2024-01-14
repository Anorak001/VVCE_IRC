from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('set_username')
def handle_set_username(username):
    print(f'Username set: {username}')

@socketio.on('send_message')
def handle_send_message(data):
    message = data.get('message', '')
    username = data.get('username', 'example_user')
    print(f'Received message from {username}: {message}')
    emit('receive_message', {'username': username, 'message': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)

