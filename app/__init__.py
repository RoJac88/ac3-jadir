from flask import Flask
from config import Config
from db import PostgresDB

db = PostgresDB()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)

    from app.home import bp as home_bp
    app.register_blueprint(home_bp)

    from app.alunos import bp as alunos_bp
    app.register_blueprint(alunos_bp, url_prefix='/alunos')

    return app
