import argparse
import threading, webbrowser

try:
    from cheroot.wsgi import Server as WSGIServer, PathInfoDispatcher
except ImportError:
    from cherrypy.wsgiserver import CherryPyWSGIServer as WSGIServer, WSGIPathInfoDispatcher as PathInfoDispatcher

from pelican_cms import app

def run_debug_server() -> None:
    try:
        port = 5000
        
        threading.Timer(1.25, lambda: webbrowser.open(f'http://127.0.0.1:{port}') ).start()
        
        app.run('0.0.0.0', port=port, debug=True)
        
    except KeyboardInterrupt:
        return


def run_production_server() -> None:
    import random

    port = 5000 + random.randint(0, 999)
    url = f"http://127.0.0.1:{port}"

    try:
        d = PathInfoDispatcher({'/': app})
        server = WSGIServer(('127.0.0.1', port), d)
        threading.Timer(1.25, lambda: webbrowser.open(url) ).start()
        server.start()
        
    except KeyboardInterrupt:
        server.stop()
        return


if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    parser.add_argument('--debug', action="store_true")

    args = parser.parse_args()

    if args.debug:
        run_debug_server()
    else:
        run_production_server()
