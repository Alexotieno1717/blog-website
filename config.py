import os


class Config:
    """
    General configuration parent class
    """
    SECRET_KEY = 'alexotieno900'
    # SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    QUOTE_API_BASE_URL = 'http://quotes.stormconsultancy.co.uk/random.json'


class ProdConfig(Config):
    """
    Production configuration
    """


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:alex17176251@localhost/blog'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
}
