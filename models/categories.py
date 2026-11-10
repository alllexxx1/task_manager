from db import get_connection


def list_categories() -> list[dict]:
    with get_connection() as connection:
        return connection.execute("SELECT id, name FROM categories ORDER BY id").fetchall()
