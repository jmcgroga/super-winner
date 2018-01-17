class Config(object):
    DEBUG = False
    TESTING = False
    BLUEPRINT_ROOT_URL_PREFIX = '/'
    BLUEPRINT_ROOT_EDITOR_PREFIX = '/editor'
    BLUEPRINT_ROOT_API_PREFIX = '/api'
    AGGREDIT_URL_PREFIX = "/aggredit/js"
    DOCUMENT_DIR = None
    
class Production(Config):
    pass

class Development(Config):
    DEBUG = True
    BLUEPRINT_ROOT_URL_PREFIX = '/aggredit'
    BLUEPRINT_ROOT_EDITOR_PREFIX = '/aggredit/editor'
    BLUEPRINT_ROOT_API_PREFIX = '/aggredit/api'
    AGGREDIT_URL_PREFIX = "http://localhost:8000/js"
    DOCUMENT_DIR = '../documents'

class Testing(Config):
    TESTING = True
    BLUEPRINT_ROOT_URL_PREFIX = '/aggredit'
    BLUEPRINT_ROOT_EDITOR_PREFIX = '/aggredit/editor'
    BLUEPRINT_ROOT_API_PREFIX = '/aggredit/api'
    AGGREDIT_URL_PREFIX = "http://localhost:8000/js"
    DOCUMENT_DIR = None
