from . import api
from aggredit.models import *

from uuid import uuid4

from flask import render_template, request, abort, jsonify

@api.route('/')
def index():
    return render_template("api/index.html")

@api.route('/documents', methods=['GET'])
def get_documents():
    return jsonify(documents)

@api.route('/documents/<document>', methods=['GET'])
def load_document(document):
    items = Documents.appdoc().loadDocument(document)

    return jsonify(
        { 'document': document,
          'items': items
        }
    )

@api.route('/documents', methods=['POST'])
def save_document():
    if not request.json or 'document' not in request.json or 'items' not in request.json:
        abort(400)

    document = request.json['document']
    items = request.json['items']

    Documents.appdoc().saveDocument(document, items)

    return jsonify({ 'saved' : True })

@api.route('/uuids', methods=['GET'])
def get_uuids():
    return jsonify({
        'uuids' : [ str(uuid4()) for i in range(0, 10)]
    })

