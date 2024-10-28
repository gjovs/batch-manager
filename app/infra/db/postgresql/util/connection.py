from psycopg2 import OperationalError, connect

from app.config import Config


def create_connection():
    try:
        connection = connect(
            host=Config.DATABASE.get('DB_HOST'),
            port=Config.DATABASE.get('DB_PORT'),
            dbname=Config.DATABASE.get('DB_NAME'),
            user=Config.DATABASE.get('DB_USER'),
            password=Config.DATABASE.get('DB_PASSWORD')
        )
        return connection
    except OperationalError as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None
    