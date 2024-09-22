from flask import Flask, render_template
from services.schedule import get_schedule, get_clock_ins
from services.get_weeks import get_current_week, get_current_week_schedule

app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        'index.html',
        current_week_schedule=get_current_week_schedule()
    )

@app.route('/schedule')
def schedule():
    schedule = get_schedule()

    return schedule

@app.route('/clock_ins')
def clock_ins():
    clock_ins = get_clock_ins()

    return clock_ins