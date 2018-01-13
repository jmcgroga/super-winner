from flask import Blueprint

editor = Blueprint('editor',
                __name__,
                url_prefix='/editor',
                template_folder='templates',
                static_folder='static')

from . import views