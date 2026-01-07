"""
Part 6: Homework - Personal To-Do List App
==========================================
See Instruction.md for full requirements.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample Data (In-memory list)
TASKS = [
    {'id': 1, 'title': 'Learn Flask', 'status': 'Completed', 'priority': 'High'},
    {'id': 2, 'title': 'Build To-Do App', 'status': 'In Progress', 'priority': 'Medium'},
    {'id': 3, 'title': 'Push to GitHub', 'status': 'Pending', 'priority': 'Low'},
]

@app.route('/')
def index():
    # Renders the index.html template and passes the TASKS list
    return render_template('index.html', tasks=TASKS)

@app.route('/task/<int:task_id>')
def task_detail(task_id):
    # Finds a specific task by its ID
    task = next((t for t in TASKS if t['id'] == task_id), None)
    return render_template('task.html', task=task)

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        # Logic to add a new task from the form
        new_task = {
            'id': len(TASKS) + 1,
            'title': request.form.get('title'),
            'status': 'Pending',
            'priority': request.form.get('priority')
        }
        TASKS.append(new_task)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)