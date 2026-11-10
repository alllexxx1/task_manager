from db import get_connection


def list_tasks() -> list[dict]:
    query = """
            SELECT tasks.*, categories.name AS category_name,
                    priorities.name AS priority_name, statuses.name AS status_name
            FROM tasks
            JOIN categories ON categories.id = tasks.category_id
            JOIN priorities ON priorities.id = tasks.priority_id
            JOIN statuses ON statuses.id = tasks.status_id
    """

    with get_connection() as connection:
        return connection.execute(query).fetchall()


def get_task(task_id: int) -> dict | None:
    query = """
            SELECT tasks.*, categories.name AS category_name,
                    priorities.name AS priority_name, statuses.name AS status_name
            FROM tasks
            JOIN categories ON categories.id = tasks.category_id
            JOIN priorities ON priorities.id = tasks.priority_id
            JOIN statuses ON statuses.id = tasks.status_id
            WHERE tasks.id = %s
    """

    with get_connection() as connection:
        return connection.execute(query, (task_id,)).fetchone()
