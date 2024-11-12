from dataclasses import dataclass
from typing import Dict


@dataclass
class Group:
    students: Dict[str, int]