from flask import Flask, render_template
from flask_socketio import SocketIO, emit


app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'topsecret'
socketio = SocketIO( app )


@app.route('/')
def index():
    return render_template('./index.html')


@socketio.on('my event')
def myevent(json):
    print('received message: ' + str(json))
    socketio.emit('my response', json)



if __name__ == '__main__':
    socketio.run( app, debug=True, port=5000 )
