"""
Part 3: Jinja2 Variables - Passing Data from Python to HTML
============================================================
How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template

app = Flask(__name__)

# ---------------- HOME ----------------

@app.route('/')
def home():
    return render_template(
        'index.html',
        title="MCA Student | Python & Flask Enthusiast | AI Learner",
        name="Nikita",
        course="MCA",
        college="Your College",
        focus="Flask & Jinja2"
    )


# ---------------- PROFILE ----------------

@app.route('/profile')
def profile():
    return render_template(
        'profile.html',
        name="Sarah",
        age=22,
        course="Web Development",
        email="sarah@email.com",
        city="Pune",
        is_enrolled=True
    )


# ---------------- SKILLS ----------------

@app.route('/skills')
def skills():
    skills_list = ['Python', 'HTML', 'CSS', 'JavaScript', 'Flask']
    return render_template('skills.html', skills=skills_list)

# ---------------- PROJECTS ----------------

@app.route('/projects')
def projects():
    project_list = [
        {'name': 'Personal Website', 'status': 'Completed', 'tech': 'HTML/CSS'},
        {'name': 'Flask Blog', 'status': 'In Progress', 'tech': 'Python/Flask'},
        {'name': 'Weather App', 'status': 'Planned', 'tech': 'JavaScript'}
    ]
    return render_template('projects.html', projects=project_list)


if __name__ == '__main__':
    app.run(debug=True)


# =============================================================================
# JINJA2 SYNTAX QUICK REFERENCE:
# =============================================================================
#
# {{ variable }}          - Output a variable
# {{ variable|upper }}    - Use a filter (uppercase)
# {{ variable|default('N/A') }} - Default value if variable is empty
#
# {% if condition %}      - If statement
#   ...
# {% endif %}
#
# {% for item in list %}  - For loop
#   {{ item }}
# {% endfor %}
#
# =============================================================================

# =============================================================================
# EXERCISES:
# =============================================================================
#
# Exercise 3.1: Add more data
#   - Add more fields to the profile (email, city, etc.)
#   - Display them in profile.html
#
# Exercise 3.2: Conditional display
#   - In profile.html, show "Enrolled" or "Not Enrolled" based on is_enrolled
#   - Use {% if is_enrolled %} ... {% else %} ... {% endif %}
#
# Exercise 3.3: Create a grades page
#   - Create a new route /grades
#   - Pass a dictionary of subjects and grades
#   - Display them in a table using a for loop
#
# =============================================================================
