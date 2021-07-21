from flask import Flask, render_template
from marvel_project.config import Config
from .api.routes import api
from .site.routes import site
from .authentication.routes import auth
from Flask_Cors import CORS

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from marvel_project.models import db as root_db, login_manager, ma
from marvel_project.helpers import JSONEncoder

app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(auth)
app.register_blueprint(api)

app.json_encoder = JSONEncoder
app.config.from_object(Config)
root_db.init_app(app)
login_manager.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)

CORS(app)

import marvel_project.models