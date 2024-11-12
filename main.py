from typing import List
from entities.schedule import Lesson
from entities.load import load_json

def main():
    schedule = load_json('output-2024-01-01-2024-11-30.json', List[Lesson])
    print(schedule[-1].name)

if __name__ == '__main__':
    main()

