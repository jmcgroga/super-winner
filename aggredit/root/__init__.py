from flask import Blueprint

root = Blueprint('root',
                __name__,
                url_prefix='/',
                template_folder='templates',
                static_folder='static')

from . import views