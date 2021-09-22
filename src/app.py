from flask import Flask
from .config import app_config


def create_app(env_name):
    """
    Create app
    """

    app = Flask(__name__)  # app initialization

    app.config.from_object(app_config[env_name])


    @app.route('/',methods=['GET'])
    def index():
        return 'Congratulations! Your first endpoint is workin'


    return app
