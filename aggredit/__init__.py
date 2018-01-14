from flask import Flask

from .root import root
from .editor import editor
from .api import api
# {{ module_import }}

app = Flask(__name__)
app.register_blueprint(root, url_prefix='/')
app.register_blueprint(editor, url_prefix='/editor')
app.register_blueprint(api, url_prefix='/api')
# {{ module_blueprint }}
