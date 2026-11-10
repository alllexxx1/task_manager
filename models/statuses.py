from db import get_connection


def list_statuses() -> list[dict]:
    with get_connection() as connection:
        return connection.execute("SELECT id, code, name FROM statuses ORDER BY id").fetchall()
