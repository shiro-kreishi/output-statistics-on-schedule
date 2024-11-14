from datetime import datetime

from entities.schedule import Schedule, Lesson


def sorting_by_date(date: datetime.date, schedules: list[Lesson], auditoriums: list[str]) -> list[Lesson]:
    schedule_for_current_date = []
    for schedule in schedules:
        current_date = datetime.strptime(schedule.date, '%Y-%m-%d').date()
        if current_date == date and schedule.auditorium in auditoriums:
            schedule_for_current_date.append(schedule)

    return schedule_for_current_date