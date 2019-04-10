from pelican_cms import app
from flask import request

@app.route('/')
def index():
    return 'Hello World!'


@app.route('/shutdown')
def shutdown():
    shutdown_server()
    return "Server is going down"

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise KeyboardInterrupt('Shutting down server...')
    func()
    
