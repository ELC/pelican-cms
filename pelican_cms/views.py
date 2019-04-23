import os
from flask import current_app, request, Blueprint, render_template

home = Blueprint('home', __name__, url_prefix='/')

@home.route('/')
def index():
    return 'Hello World! <a href="/shutdown">Apagar</a>'


@home.route('/shutdown')
def shutdown():
    
    def shutdown_server():
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise KeyboardInterrupt('Shutting down server...')
        func()

    shutdown_server()
    return "Server is going down"

@home.route('/init')
def first_time():
    
    exists = os.path.isfile(current_app.config["DATABASE_PATH"])

    if exists:
        return "Database Already Created"
    
    else:
        from pelican_cms.models import db
        
        db.create_all()
        
        return "Database Created"
