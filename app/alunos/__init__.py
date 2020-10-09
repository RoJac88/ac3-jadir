from flask import Blueprint

bp = Blueprint('alunos', __name__)

from app.alunos import routes
