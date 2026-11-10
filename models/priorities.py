from db import get_connection


def list_priorities() -> list[dict]:
    with get_connection() as connection:
        return connection.execute("SELECT id, code, name FROM priorities ORDER BY id").fetchall()
