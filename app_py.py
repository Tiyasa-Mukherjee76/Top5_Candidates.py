# -*- coding: utf-8 -*-
"""app.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1GylBqYk7Usb37Wa9gS0u23Dbu20vi26t
"""

!pip install flask pyngrok

import os
if not os.path.exists("templates"):
  os.mkdir("templates")
  print("templates/folder created")

from google.colab import drive
drive.mount('/content/drive')

from pyngrok import ngrok

ngrok.set_auth_token("2zsve1FwR3AUapLUMsQz1nMNOUQ_3FSXzhcDeBrfCmgWsQVyB")

import os

os.makedirs('templates', exist_ok=True)

with open("templates/home.html", "w") as f:
    f.write("""
<!doctype html>
<html>
<head>
  <title>Hiring App - Home</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="container">
<h1 class="mt-4">Welcome to the Hiring App</h1>
<p>Choose an option below:</p>
<a href="{{ url_for('list_candidates')}}" class="btn btn-primary mt-4">List Candidates</a>
<a href="{{ url_for('top5')}}" class="btn btn-success">Top 5 Candidates</a>
</body>
</html>
""")
print("home.html created")

with open("templates/candidates.html", "w") as f:
    f.write("""
<!doctype html>
<html>
<head>
  <title>All Candidates</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="container">
<h1 class="mt-4">All candidates (sorted by score)</h1>
<table class="table table-bordered">
<thead>
<tr>
  <th>Name</th><th>Experience</th><th>Education</th><th>Skills</th><th>Score</th>
</tr>
</thead>
<tbody>
{% for c in candidates %}
<tr>
  <td>{{ c.get('name') }}</td>
  <td>{{ c.get('years_experience') }}</td>
  <td>{{ c.get('education') }}</td>
  <td>{{ c.get('skills') | join(', ') }}</td>
  <td>{{ c.get('score') }}</td>
</tr>
{% endfor %}
</tbody>
</table>
<a href="{{ url_for('home')}}" class="btn btn-secondary">Back</a>
<a href="{{ url_for('top5')}}" class="btn btn-success">Top 5 Candidates</a>
</body>
</html>
""")
print("candidates.html created")

with open("templates/top5.html", "w") as f:
    f.write("""
<!doctype html>
<html>
<head>
  <title>Top 5 Hires</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
</head>
<body class="container">
<h1 class="mt-4">Top 5 Candidates to hire</h1>
<table class="table table-bordered">
<thead>
<tr>
  <th>Name</th><th>Experience</th><th>Education</th><th>Skills</th><th>Score</th><th>Reason</th>
</tr>
</thead>
<tbody>
{% for c in candidates %}
<tr>
  <td>{{ c.get('name') }}</td>
  <td>{{ c.get('years_experience') }}</td>
  <td>{{ c.get('education') }}</td>
  <td>{{ c.get('skills') | join(', ') }}</td>
  <td>{{ c.get('score') }}</td>
  <td>{{ c.get('reason') }}</td>
</tr>
{% endfor %}
</tbody>
</table>
<a href="{{ url_for('home')}}" class="btn btn-secondary">Back</a>
</body>
</html>
""")
print("top5.html created")

import json

sample_candidates = [
    {"name": "Alice", "years_experience": 5, "education": "Masters", "skills": ["Python", "AI"]},
    {"name": "Bob", "years_experience": 2, "education": "Bachelors", "skills": ["Java"]},
    {"name": "Charlie", "years_experience": 7, "education": "PhD", "skills": ["Python", "ML", "Java"]},
    {"name": "Diana", "years_experience": 1, "education": "Bachelors", "skills": ["AI"]},
    {"name": "Eve", "years_experience": 3, "education": "Masters", "skills": ["Python", "Java", "ML"]},
    {"name": "Frank", "years_experience": 4, "education": "Masters", "skills": ["Python", "AI", "ML"]}
]
with open('form-submissions.json', 'w') as f:
    json.dump(sample_candidates, f)
print("form-submissions.json created")

from flask import Flask, render_template
import json
from pyngrok import ngrok

app = Flask(__name__, template_folder='templates')

# Load candidate data
with open('form-submissions.json', 'r') as f:
    candidates = json.load(f)

# Scoring function
def score_candidate(candidate):
    score = 0
    score += 3 * candidate.get('years_experience', 0)
    skills = candidate.get('skills', [])
    wanted_skills = ['Python', 'Java', 'AI', 'ML']
    score += 5 * len([s for s in skills if s in wanted_skills])
    if candidate.get('education') in ['Masters', 'PhD']:
        score += 5
    return score

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/candidates')
def list_candidates():
    scored = []
    for c in candidates:
        c['score'] = score_candidate(c)
        scored.append(c)
    scored.sort(key=lambda x: x['score'], reverse=True)
    return render_template('candidates.html', candidates=scored)

@app.route('/top5')
def top5():
    scored = []
    for c in candidates:
        c['score'] = score_candidate(c)
        scored.append(c)
    scored.sort(key=lambda x: x['score'], reverse=True)
    selected = scored[:5]
    for c in selected:
        c['reason'] = f"High score: {c['score']}, strong skills & experience."
    return render_template('top5.html', candidates=selected)

# Start ngrok and Flask
ngrok.set_auth_token("2zsve1FwR3AUapLUMsQz1nMNOUQ_3FSXzhcDeBrfCmgWsQVyB")  # your token
public_url = ngrok.connect(5000)
print(" * ngrok tunnel:", public_url)

app.run(port=5000)