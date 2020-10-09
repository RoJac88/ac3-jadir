from flask import request, jsonify
from app import db
from dao import read_aluno, read_alunos, create_aluno, delete_aluno
from app.alunos import bp


@bp.route('/')
def ver_alunos():
    alunos = read_alunos()
    return jsonify(alunos)


@bp.route('/<int:ra>/', methods=['GET', 'DELETE'])
def ver_aluno(ra):
    aluno = read_aluno(ra)
    if not aluno or len(aluno) == 0:
        return {}, 404
    if request.method == 'GET':
        return aluno
    delete_aluno(ra)
    return {'message': f'aluno {ra} removido'}


@bp.route('/<int:ra>', methods=['PUT'])
def add_aluno():
    aluno = read_aluno(ra)
    if aluno or len(aluno) > 0:
        return {}, 409
    f = request.form
    try:
        if 'complemento' in f:
            args = (ra, f['nome_aluno'], f['email'], f['logadouro'], f['numero'], f['cep'], f['complemento'])
        else:
            args = (ra, f['nome_aluno'], f['email'], f['logadouro'], f['numero'], f['cep'])
        aluno = create_aluno(*args)
    except KeyError as e:
        print(e)
        return {}, 400
    return jsonify(aluno)
