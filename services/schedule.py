from database.main import get_db
from datetime import datetime, timedelta

def get_schedule(start_date=None, end_date=None):
    now = datetime.now()
    db = get_db()
    schedule = None

    if start_date and end_date:
        schedule = db.execute('''
            SELECT date_name, name, day, month, year,
            start_hour, start_minute, end_hour, end_minute
            FROM schedules
            WHERE month = ? AND (day BETWEEN ? AND ?)
        ''', (now.month, start_date, end_date)).fetchall()
    else:
        schedule = db.execute('''
            SELECT date_name, name, day, month, year,
            start_hour, start_minute, end_hour, end_minute
            FROM schedules
            WHERE month = ?
        ''', (now.month,)).fetchall()

    json_schedule = []

    if len(schedule) < 1:
        return {"error": "No hay horarios programados para este mes... O algo se rompió 🚧"}
    
    for day in schedule:
        json_schedule.append({
            'date_name': day[0],
            'name': day[1],
            'day': day[2],
            'month': day[3],
            'year': day[4],
            'start_hour': day[5],
            'start_minute': day[6],
            'end_hour': day[7],
            'end_minute': day[8]
        })

    return json_schedule
    
def get_clock_ins():
    now = datetime.now()
    db = get_db()
    clock_ins = db.execute('''
        SELECT date_name, name, day, month, year,
        hour, minute, second
        FROM clock_in
        WHERE month = ?
    ''', (now.month,)).fetchall()

    schedules = get_schedule()

    clock_ins_json = []

    if len(clock_ins) < 1:
        return {"error": "No hay horarios programados para este mes... O algo se rompió 🚧"}
    
    for clock_in in clock_ins:
        clock_ins_json.append({
            'date_name': clock_in[0],
            'name': clock_in[1],
            'day': clock_in[2],
            'month': clock_in[3],
            'year': clock_in[4],
            'hour': clock_in[5],
            'minute': clock_in[6],
            'second': clock_in[7],
        })

    


    return clock_ins_json


def get_clock_outs():
    ...


def get_breaks():
    ...