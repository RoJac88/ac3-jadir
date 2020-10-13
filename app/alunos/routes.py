from flask import request, render_template, jsonify, abort
from app import db
from dao import read_aluno, read_alunos, create_aluno, delete_aluno
from app.alunos import bp


@bp.route('/')
def ver_alunos():
    alunos = read_alunos()
    return render_template('view_alunos.html', alunos=alunos)


@bp.route('/<int:ra>/', methods=['GET', 'DELETE'])
def ver_aluno(ra):
    aluno = read_aluno(ra)
    if not aluno or len(aluno) == 0:
        abort(404)
    if request.method == 'GET':
        return render_template('view_aluno.html', aluno=aluno)
    delete_aluno(ra)
    return {'message': f'aluno {ra} removido'}


@bp.route('/<int:ra>', methods=['PUT'])
def add_aluno(ra):
    aluno = read_aluno(ra)
    if aluno:
        return {}, 409
    f = request.form
    args = (ra, f['nome'], f['email'], f['log'], f['num'], f['cep'], f['comp'])
    print(args)
    aluno = create_aluno(*args)
    return render_template('view_aluno.html', aluno=aluno)
