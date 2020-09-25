from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

bootstrap = Bootstrap()
db = SQLAlchemy()


def create_app(config_name):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(config_options.get(config_name))

    # Initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    from app.main import main
    # from app.auth import auth
    # app.register_blueprint(auth)
    from app.auth import auth as auth_blueprint
    app.register_blueprint(main)
    app.add_url_rule('/', endpoint='main.index')
    app.register_blueprint(auth_blueprint, url_prefix='/authenticate')

    return app
