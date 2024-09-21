from database.main import get_db
from datetime import datetime, timedelta

def get_schedule():
    now = datetime.now()
    db = get_db()
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
    ...


def get_clock_outs():
    ...


def get_breaks():
    ...