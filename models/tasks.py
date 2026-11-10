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


def create_task(task: dict) -> int:
    with get_connection() as connection:
        row = connection.execute(
            """
            INSERT INTO tasks (title, description, category_id, priority_id, status_id)
            VALUES (%s, %s, %s, %s, %s) RETURNING id
            """,
            (task["title"], task["description"], task["category_id"],
             task["priority_id"], task["status_id"]),
        ).fetchone()
        return row["id"]


def update_task(task_id: int, task: dict) -> None:
    with get_connection() as connection:
        connection.execute(
            """
            UPDATE tasks SET title = %s, description = %s, category_id = %s,
                             priority_id = %s, status_id = %s
            WHERE id = %s
            """,
            (task["title"], task["description"], task["category_id"],
             task["priority_id"], task["status_id"], task_id),
        )

def delete_task(task_id: int) -> None:
    with get_connection() as connection:
        connection.execute("DELETE FROM tasks WHERE id = %s", (task_id,))
