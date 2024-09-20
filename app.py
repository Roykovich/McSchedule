from flask import Flask, render_template
from database.main import get_db

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule')
def schedule():
    db = get_db()
    schedule = db.execute('SELECT date_name, name, day, month, year, start, end FROM schedules WHERE month = ?', ('septiembre',)).fetchall()
    json_schedule = []

    if len(schedule) < 1:
        return 'No hay horarios programados para septiembre'

    for day in schedule:
        json_schedule.append({
            'date_name': day[0],
            'name': day[1],
            'day': day[2],
            'month': day[3],
            'year': day[4],
            'start': day[5],
            'end': day[6]
        })

    return json_schedule
