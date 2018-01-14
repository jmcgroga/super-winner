class Config(object):
    DEBUG = False
    TESTING = False
    BLUEPRINT_ROOT_URL_PREFIX = '/'
    BLUEPRINT_ROOT_EDITOR_PREFIX = '/editor'
    BLUEPRINT_ROOT_API_PREFIX = '/api'
    
class Production(Config):
    pass

class Development(Config):
    DEBUG = True
    BLUEPRINT_ROOT_URL_PREFIX = '/aggredit'
    BLUEPRINT_ROOT_EDITOR_PREFIX = '/aggredit/editor'
    BLUEPRINT_ROOT_API_PREFIX = '/aggredit/api'

class Testing(Config):
    TESTING = True
