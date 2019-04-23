from pyfladesk import init_gui
from pelican_cms import create_app

if __name__ == '__main__':
    init_gui(create_app())
