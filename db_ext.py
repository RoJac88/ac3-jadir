import os
from main import app
from app import db
from psycopg2.errors import UndefinedTable, SyntaxError, DatabaseError
from dao import read_table_columns
import csv
import glob

basedir = os.path.abspath(os.path.dirname(__file__))


def run_sql():
    for f in glob.glob(os.path.join(app.config.get('SQL_DIR'), '*.sql')):
        with open(f, 'r') as src:
            sql = src.read()
        print('Executing script:', f)
        try:
            db.execute(sql)
        except SyntaxError as e:
            print('SYNTAX ERROR executing script:', f)
            print(e)
            print('Aborting...')
            return
        except DatabaseError as e:
            print(e)
            return


def export_csv(tablename, out_path=None):
    if out_path is None:
        out_path = os.path.join(basedir, tablename + '.csv')
    try:
        cols = db.query('SELECT * FROM ' + tablename)
    except UndefinedTable:
        print('Table {} does not exist'.format(tablename))
        return
    if len(cols) > 0:
        with open(out_path, 'w', encoding='utf8', newline='') as out:
            csv_writter = csv.DictWriter(out, cols[0].keys(), delimiter=';')
            csv_writter.writeheader()
            csv_writter.writerows(cols)
    else:
        print('No records found in table:', tablename)


def import_csv(csv_path, tablename=None):
    if not os.path.isfile(csv_path):
        print('File not found:', csv_path)
        return
    if not csv_path[-4:] == '.csv':
        print('Invalid input file', csv_path)
        return
    if tablename is None:
        tablename = os.path.basename(csv_path)[:-4]
    columns = [c.get('column_name') for c in read_table_columns(tablename)]
    if len(columns) == 0:
        print(tablename, 'table has no columns or does not exist')
        return
    with open(csv_path, 'r', encoding='utf8', newline='') as in_file:
        csv_reader = csv.DictReader(in_file, delimiter=';')
        head = set(csv_reader.fieldnames).intersection(set(columns))
        if len(head) == 0:
            print("CSV headers do not match any of table: {}'s column names: {}".format(tablename, columns))
        for row in csv_reader:
            vals = [row[h] for h in head]
            sql = 'INSERT INTO {} ({}) VALUES ({})'.format(tablename, ', '.join(head), ', '.join(('%s' for h in head)))
            try:
                db.execute(sql, args=vals)
            except DatabaseError as e:
                print('Database error on row:', str(row.values()))
                print(e)


if __name__ == '__main__':

    with app.app_context():
        run_sql()
