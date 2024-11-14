from datetime import datetime
from entities.group import UnicPairsGroup

from entities.schedule import Schedule, Lesson

def clean_duplicates_group(date: datetime.date, schedules: list[Lesson], auditoriums: list[str], groups: dict[str, int]):
    unic = []
    unic_groups = []
    for schedule in schedules:
        current_date = datetime.strptime(schedule.date, '%Y-%m-%d').date()
        if current_date == date and schedule.auditorium in auditoriums:
            if not schedule.group in unic_groups:
                unic_groups.append(schedule.group)
                unic_pairs = UnicPairsGroup(
                    schedule.group,
                    groups[schedule.group],
                    [schedule.name],
                    schedule.auditorium,
                    current_date,
                )
                unic_groups.append(unic_pairs)
            else:
               for g in unic_groups:
                   if g.group_name == schedule.group:
                       g.pair_names.append(schedule.name)

    return unic_groups