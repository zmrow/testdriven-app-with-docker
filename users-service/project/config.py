# config for the users app


class BaseConfig:
    '''Base config'''
    DEBUG = False
    TESTING = False


class DevelopmentConfig(BaseConfig):
    '''Dev config'''
    DEBUG = True
    TESTING = True


class TestingConfig(BaseConfig):
    '''Testing config'''
    DEBUG = True
    TESTING = True


class ProductionConfig(BaseConfig):
    '''Prod config'''
    DEBUG = False
