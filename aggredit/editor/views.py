from . import editor
from aggredit.models import *

import os

from flask import render_template, send_from_directory

@editor.route('/', defaults={ 'document': None })
@editor.route('/<document>')
def index(document):
    if document is None:
        document = 'default'
    return render_template("editor/index.html",
                           document=document)

@editor.route('/css/<path:path>')
def css(path):
    return send_from_directory(os.path.join(editor.root_path, 'static', 'css'), path)

@editor.route('/js/<path:path>')
def js(path):
    return send_from_directory(os.path.join(editor.root_path, 'static', 'js'), path)

