from flask import Flask

app = Flask(__name__)
version = "0.0.1"

from pelican_cms.views import *
