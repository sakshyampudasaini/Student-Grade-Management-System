"""Module defining the Student dataclass data model."""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Student:
    """Data class representing a student and their academic marks."""

    student_id: str
    name: str
    marks: Dict[str, float] = field(default_factory=dict)

    def add_or_update_mark(self, subject: str, score: float) -> None:
        """Add a new subject mark or update an existing one."""
        self.marks[subject] = score

    def remove_mark(self, subject: str) -> bool:
        """Remove a subject mark. Returns True if removed, False if subject was not found."""
        if subject in self.marks:
            del self.marks[subject]
            return True
        return False