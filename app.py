from flask import Flask, render_template
from services.schedule import get_schedule

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule')
def schedule():
    schedule = get_schedule()

    return schedule
