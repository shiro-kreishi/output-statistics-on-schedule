from typing import List, Dict
from entities.schedule import Lesson
from entities.load import load_json
from entities.group import Group


def main():
    schedule = load_json('output-2024-01-01-2024-11-30.json', List[Lesson])
    print(schedule[-1].name)
    groups = load_json('groups-data.json', Dict[str, int])
    print(groups["430Б"])


if __name__ == '__main__':
    main()

