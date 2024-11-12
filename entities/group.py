from dataclasses import dataclass
from typing import Dict


@dataclass
class ClassData:
    students: Dict[str, int]