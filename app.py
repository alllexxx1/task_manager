from flask import Flask, render_template, request, redirect, url_for

from models.tasks import list_tasks, get_task, create_task
from models.categories import list_categories
from models.priorities import list_priorities
from models.statuses import list_statuses

app = Flask(__name__, template_folder='./templates')


def validate_task(task: dict, category_list: list[dict],
                  priority_list: list[dict], status_list: list[dict]) -> str:
    if not task["title"]:
        return "Введите название задачи."
    if task["category_id"] not in [str(category["id"]) for category in category_list]:
        return "Выберите существующую категорию."
    if task["priority_id"] not in [str(priority["id"]) for priority in priority_list]:
        return "Выберите существующий приоритет."
    if task["status_id"] not in [str(status["id"]) for status in status_list]:
        return "Выберите существующий статус."
    return ""

@app.route('/tasks')  # https://localhost:500/tasks
def index():
    tasks = list_tasks()
    return render_template('index.html', tasks=tasks)


@app.route('/tasks/<int:task_id>')  # https://localhost:500/tasks/3
def detail(task_id: int):
    task = get_task(task_id)
    print(task)
    return render_template('detail.html', task=task)


@app.route('/tasks/new', methods=["GET", "POST"])
def create():
    category_list = list_categories()
    priority_list = list_priorities()
    status_list = list_statuses()
    task = {"title": "", "description": "", "category_id": "", "priority_id": "", "status_id": ""}
    error = ''

    if request.method == 'POST':
        task = {
            "title": request.form.get("title", "").strip(),
            "description": request.form.get("description", ""),
            "category_id": request.form.get("category_id", ""),
            "priority_id": request.form.get("priority_id", ""),
            "status_id": request.form.get("status_id", ""),
        }
        error = validate_task(task, category_list, priority_list, status_list) # None

        if not error:
            task_id = create_task(task)
            return redirect(url_for('detail', task_id=task_id))

    return render_template('form.html', task=task, error=error,
                           categories=category_list, priorities=priority_list, statuses=status_list)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
