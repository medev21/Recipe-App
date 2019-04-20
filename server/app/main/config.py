import os

# sets the path where config live ../server/app/main
base_dir = os.path.abspath(os.path.dirname(__file__))

class Config:
    #SECRET_KEY = os.getenv('SECRET_KEY')
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    DEBUG = False

class ProductionConfig(Config):
    DEBUG = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

# key = Config.SECRET_KEY