from flask import Flask
from .config import app_config
from .models import bcrypt, db
from .views.UserView import user_api as user_blueprint

def create_app(env_name):
    """
    Create app
    """

    app = Flask(__name__)  # app initialization

    app.config.from_object(app_config[env_name])

    # initializing bcrypt
    bcrypt.init_app(app)

    db.init_app(app)
    app.register_blueprint(user_blueprint, url_prefix='/api/v1/users')

    @app.route('/', methods=['GET'])
    def index():
        return 'Congratulations! Your first endpoint is workin'

    return app
