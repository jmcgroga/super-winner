from . import root
from aggredit.models import *

from flask import render_template

@root.route('/')
def index():
    return render_template("root/index.html")