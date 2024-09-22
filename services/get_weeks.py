from datetime import datetime
from calendar import monthcalendar, weekday
from services.schedule import get_schedule
import json

WEEKDAYS = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}

dias_semana = {
    'Monday': 'lunes',
    'Tuesday': 'martes',
    'Wednesday': 'miércoles',
    'Thursday': 'jueves',
    'Friday': 'viernes',
    'Saturday': 'sábado',
    'Sunday': 'domingo',
}

def get_week_by_date(selected_year, selected_month, selected_day):
    weeks = monthcalendar(selected_year, selected_month)
    current_week = {
        'number': None,
        'start_date': None,
        'end_date': None,
        'list': []
    }

    for index, week in enumerate(weeks):
        if selected_day in week:
            # current_weekday = WEEKDAYS[weekday(selected_year, selected_month, selected_day)]
            # print(f"[+] Day {selected_day} [{current_weekday}] is in week {index + 1}")
            # print(f"[+] Week {index + 1} is from {week[0]} to {week[-1]}\n")
            current_week['number'] = index + 1
            current_week['start_date'] = week[0]
            current_week['end_date'] = week[-1]
            for day in week:
                current_week['list'].append(datetime(selected_year, selected_month, day))        
            break   


    # print(f"Current week: {current_week}")
    # for day in current_week:
    #     print(f"Day: {day.strftime('%Y-%b-%d')} [{WEEKDAYS[weekday(day.year, day.month, day.day)]}]")
    # print(current_week)
    return current_week

def get_current_week():
    now = datetime.now()
    return get_week_by_date(now.year, now.month, 15)
    return get_week_by_date(now.year, now.month, now.day)

def get_current_week_schedule():
    current_week = get_current_week()
    schedule = get_schedule(
        start_date=current_week['start_date'],
        end_date=current_week['end_date']
    )

    current_week_schedule = []

    for day in current_week['list']:
        for index, schedule_day in enumerate(schedule):
            if day.day == schedule_day['day']:
                current_week_schedule.append({
                    'date_name': schedule_day['date_name'],
                    'name': schedule_day['name'].capitalize(),
                    'day': f'{day.day:02d}',
                    'month': schedule_day['month'],
                    'year': schedule_day['year'],
                    'start_hour': schedule_day['start_hour'],
                    'start_minute': schedule_day['start_minute'],
                    'end_hour': schedule_day['end_hour'],
                    'end_minute': schedule_day['end_minute'],
                    'formatted_date': f'{schedule_day['start_hour']:02d}:{schedule_day['start_minute']:02d} - {schedule_day['end_hour']:02d}:{schedule_day['end_minute']:02d}',
                })

                break

            if index == len(schedule) - 1:
                print(f"Day {day.day} is not in schedule")
                current_week_schedule.append({
                    'date_name': None,
                    'name': dias_semana[day.strftime('%A')].capitalize(),
                    'day': f'{day.day:02d}',
                    'month': day.month,
                    'year': day.year,
                    'start_hour': None,
                    'start_minute': None,
                    'end_hour': None,
                    'end_minute': None,
                    'formatted_date': f'Libre papá',
                })
                


    # print(json.dumps(current_week_schedule, indent=4))
    return current_week_schedule
