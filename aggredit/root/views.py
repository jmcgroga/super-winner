from . import root
from aggredit.models import *
from aggredit import editor

from flask import url_for, redirect, current_app

@root.route('/')
def index():
    return redirect(current_app.config['BLUEPRINT_ROOT_EDITOR_PREFIX'])
