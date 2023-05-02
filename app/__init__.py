from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#  gives us access to database operations by instantiating
# the db and migrate
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # __name__ stores the name of the module we're in
    app = Flask(__name__)
    
    # set up database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/flaskey_development'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'    
    
    # connect the db and migrate to our flask app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # import routes
    from .routes import crystal_bp
    
    # register the blueprint
    app.register_blueprint(crystal_bp)
    
    # import model
    from app.models.crystal import Crystal

    return app

