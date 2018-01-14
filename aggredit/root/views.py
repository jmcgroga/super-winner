from . import root
from aggredit.models import *
from aggredit import editor

from flask import url_for, redirect

@root.route('/')
def index():
    return redirect('/aggredit/editor')
