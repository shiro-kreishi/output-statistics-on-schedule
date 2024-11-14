from datetime import datetime
from typing import List, Dict
from entities.schedule import Lesson
from entities.load import load_json
from sorting.by_date import sorting_by_date

auditoriums = ['232А', '233А', '234А', '235А']

def main():
    schedule = load_json('output-2024-01-01-2024-11-30.json', List[Lesson])
    print(schedule[-1].name)
    groups = load_json('groups-data.json', Dict[str, int])
    print(groups["430Б"])
    day = datetime.strptime('2024-11-12', '%Y-%m-%d').date()
    for i in sorting_by_date(day, schedule, auditoriums):
        print(i)


if __name__ == '__main__':
    main()

