import psycopg2
from psycopg2.extras import RealDictCursor
from flask import current_app, _app_ctx_stack


class PostgresDB(object):

    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # app.config.setdefault('POSTGRES_DB', ':memory:')
        app.teardown_appcontext(self.teardown)

    def connect(self):
        c = psycopg2.connect(**current_app.config['POSTGRES_DB'])
        c.autocommit = True
        return c

    def teardown(self, exception):
        ctx = _app_ctx_stack.top
        if hasattr(ctx, 'postgres_db'):
            ctx.postgres_db.close()

    @property
    def connection(self):
        ctx = _app_ctx_stack.top
        if ctx is not None:
            if not hasattr(ctx, 'postgres_db'):
                ctx.postgres_db = self.connect()
            return ctx.postgres_db

    def query(self, query, args=(), one=False):
        cur = self.connection.cursor(cursor_factory=RealDictCursor)
        cur.execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

    def execute(self, query, args=()):
            new_entry = None
            with self.connection as conn:
                cur = conn.cursor()
                cur.execute(query, args)
                if 'returning' in query.lower():
                    rv = cur.fetchone()[0]
                    return rv
