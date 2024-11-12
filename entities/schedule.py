from dataclasses import dataclass
from typing import List


@dataclass
class Lesson:
    name: str
    group: str
    auditorium: str
    date: str
    timestamp: str

@dataclass
class Schedule:
    lessons: List[Lesson]