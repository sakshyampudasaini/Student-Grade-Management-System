"""Module for computing student score averages, letter grades, and GPAs."""

from typing import Dict


def calculate_average(marks: Dict[str, float]) -> float:
    """Calculate the average score across all subjects for a student."""
    if not marks:
        return 0.0
    return sum(marks.values()) / len(marks)


def get_letter_grade(avg: float) -> str:
    """Convert an average score into a letter grade using a detailed scale."""
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B+"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    elif avg >= 40:
        return "D"
    return "F"


def get_gpa(avg: float) -> float:
    """Convert an average score into a standard GPA value (0.0 to 4.0 scale)."""
    if avg >= 90:
        return 4.0
    elif avg >= 80:
        return 3.6
    elif avg >= 70:
        return 3.2
    elif avg >= 60:
        return 2.8
    elif avg >= 50:
        return 2.4
    elif avg >= 40:
        return 2.0
    return 0.0