import os

from flask import Flask

from .root import root
from .editor import editor
from .api import api
# {{ module_import }}

app = Flask(__name__)
flask_config = 'aggredit.config.Production'

if 'FLASK_CONFIG' in os.environ:
    flask_config = os.environ['FLASK_CONFIG']

app.config.from_object(flask_config)
app.register_blueprint(root, url_prefix=app.config['BLUEPRINT_ROOT_URL_PREFIX'])
app.register_blueprint(editor, url_prefix=app.config['BLUEPRINT_ROOT_EDITOR_PREFIX'])
app.register_blueprint(api, url_prefix=app.config['BLUEPRINT_ROOT_API_PREFIX'])
# {{ module_blueprint }}
