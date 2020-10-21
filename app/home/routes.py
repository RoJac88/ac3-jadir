from flask import render_template
from psycopg2.errors import UndefinedTable
from dao import read_tablenames, read_table_columns, read_table_size
from app.home import bp


@bp.route('/')
def index():
    data = []
    tabelas = read_tablenames()
    for tab in tabelas:
        meta = {'schemaname': tab['schemaname'], 'owner': tab['tableowner']}
        try:
            size = int(read_table_size(tab['tablename'])['size'] / 1000)
            meta['tamanho'] = f'{size:.2f} KB'
        except UndefinedTable as e:
            print(e)
        cols = []
        for col in read_table_columns(tab['tablename']):
            cols.append({'name': col['column_name'], 'type': col['data_type'], 'max_len': col.get('character_maximum_length')})
        data.append({'name': tab['tablename'], 'cols': cols, 'meta': meta})
    return render_template('index.html', db_data=data)
