import socket
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def index():
    ip = socket.gethostbyname(socket.gethostname())
    return (f"Hello World!\n, {ip}")


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')