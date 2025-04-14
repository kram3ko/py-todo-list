# 📝 py-todo-list

A simple Django-based TODO app for managing personal tasks.

## 🚀 Features

- Create, update, and delete tasks
- Set deadlines for tasks
- Mark tasks as complete/incomplete
- Filter tasks by status (completed, pending, today)
- Tag tasks for easy categorization

## 🛠 Tech Stack

- Python 3.x
- Django 5.x
- SQLite

## ▶️ Getting Started

1. Clone the repository:
   ```bash
   git clone https://github.com/kram3ko/py-todo-list.git
   cd py-todo-list
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   pip install uv
   uv sync
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. (Optional) Load initial data:
   ```bash
   python manage.py loaddata initial_data.json
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser at `http://127.0.0.1:8000/`
