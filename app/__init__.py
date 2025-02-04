from flask import Flask
from config import config_options


def create_app(config_name):
    app = Flask(__name__)

    # Creating the app configurations
    app.config.from_object(config_options[config_name])

    # importing our blueprints
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint

    # Registering our blueprints
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/')

    return app
