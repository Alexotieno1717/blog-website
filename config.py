import os


class Config:
    """
    General configuration parent class
    """
    SECRET_KEY = 'alexotieno900'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    """
    Production configuration
    """


class DevConfig(Config):

    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}
