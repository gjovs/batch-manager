from app.infra.db.postgresql.util import create_connection

class Repository:
    def __init__(self):
        self.connection = create_connection()

    def __del__(self):
        _connection = getattr(self, 'connection', None)
        if _connection: self.connection.close()