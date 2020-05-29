from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config[ 'SECRET_KEY' ] = 'supersecret'
socketio = SocketIO( app )

@app.route('/')
def landing():
  return render_template('landing.html')

def messageRecived():
  print('Mesaj primit!')

@socketio.on('mesaj primit')
def handle_mesaj(json):
  print( 'event primit: ' + str( json ) )
  socketio.emit( 'raspuns', json, callback=messageRecived )

if __name__ == '__main__':
  socketio.run( app, debug = True )