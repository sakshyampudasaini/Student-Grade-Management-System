"""Module for managing text file storage and CSV reporting."""

import csv
import os
from typing import Dict

import grade
from student import Student

FILE_NAME = "students.txt"


def load_students() -> Dict[str, Student]:
    """Load all student records from the local storage file."""
    students: Dict[str, Student] = {}
    if not os.path.exists(FILE_NAME):
        return students

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split("|")
                if len(parts) >= 2:
                    sid, name = parts[0], parts[1]
                    st = Student(student_id=sid, name=name)
                    if len(parts) > 2 and parts[2]:
                        for item in parts[2].split(","):
                            if ":" in item:
                                sub, score = item.split(":")
                                st.add_or_update_mark(sub, float(score))
                    students[sid] = st
    return students


def save_students(students: Dict[str, Student]) -> None:
    """Save all current student records back to the local text storage file."""
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for st in students.values():
            marks_str = ",".join([f"{sub}:{score}" for sub, score in st.marks.items()])
            f.write(f"{st.student_id}|{st.name}|{marks_str}\n")


def export_to_csv(students: Dict[str, Student], filepath: str) -> None:
    """Export the student records to a formatted CSV spreadsheet file."""
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Student ID", "Name", "Average", "Letter Grade", "GPA", "Subjects"])
        for st in students.values():
            avg = grade.calculate_average(st.marks)
            marks_summary = "; ".join([f"{sub}:{score}" for sub, score in st.marks.items()])
            writer.writerow([
                st.student_id,
                st.name,
                f"{avg:.2f}",
                grade.get_letter_grade(avg),
                f"{grade.get_gpa(avg):.1f}",
                marks_summary
            ])