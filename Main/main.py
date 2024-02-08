from flask import Flask, render_template
from flask_socketio import SocketIO, send

ip_desktop = "172.17.208.1"
ip_mac = "127.0.0.1"

app = Flask(__name__)
app.config['SECRET'] = "my_secret"
socketio = SocketIO(app, cors_allowed_origins = "*")



@socketio.on("message")
def handle_message(message):
    print("Got message: " + message)
    if(message != "User_Connected"):
        send(message, broadcast = True)

@app.route('/')
def index():
    return render_template("index.html")

if (__name__ == "__main__"):
    socketio.run(app, host = ip_mac)
