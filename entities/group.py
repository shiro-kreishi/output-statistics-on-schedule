from dataclasses import dataclass
from datetime import datetime
from typing import Dict


@dataclass
class Group:
    students: Dict[str, int]

@dataclass
class UnicPairsGroup:
    group_name: str
    len: int
    pair_names: list[str]
    auditorium: str
    date: datetime.date
