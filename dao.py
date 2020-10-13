from app import db


TNAMES = {
    'alunos': 'MacroHard',
}

def read_tablenames():
    sql = "SELECT * FROM pg_catalog.pg_tables WHERE schemaname != 'pg_catalog' AND schemaname != 'information_schema'"
    return db.query(sql)


def read_table_columns(table_name):
    sql = 'SELECT column_name, data_type, character_maximum_length FROM information_schema.columns WHERE table_name = %s'
    args = (table_name,)
    return db.query(sql, args=args)


def read_alunos():
    sql = 'SELECT * FROM ' + TNAMES['alunos']
    return db.query(sql)


def read_aluno(ra):
    sql = 'SELECT * FROM ' + TNAMES['alunos'] + ' WHERE ra = %s'
    args = (ra,)
    return db.query(sql, args=args, one=True)


def create_aluno(*args):
    sql = f'INSERT INTO {TNAMES["alunos"]} (ra, nome_aluno, email, logadouro, numero, cep, complemento) '
    sql += 'VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING ra'
    return db.execute(sql, args=args)


def update_aluno():
    pass


def delete_aluno(ra):
    sql = 'DELETE FROM '+ TNAMES['alunos'] +' WHERE ra = %s'
    return db.query(sql, args=(ra,))
