"""Main entry point running the Tkinter GUI interface for Student Grade Management."""

import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog, ttk
from typing import Dict

from file_handler import export_to_csv, load_students, save_students
import grade
from student import Student


class StudentApp:
    """Tkinter graphical user interface controller for the Student Grade System."""

    def __init__(self, root: tk.Tk) -> None:
        """Initialize windows, navigation buttons, and table views."""
        self.root = root
        self.root.title("Student Grade Management System")
        self.root.geometry("880x520")

        self.students: Dict[str, Student] = load_students()

        # --- Top Action Bar ---
        top_frame = ttk.Frame(self.root, padding=10)
        top_frame.pack(fill=tk.X)

        ttk.Button(top_frame, text="Add Student", command=self.add_student).pack(side=tk.LEFT, padx=2)
        ttk.Button(top_frame, text="Edit Name", command=self.edit_student).pack(side=tk.LEFT, padx=2)
        ttk.Button(top_frame, text="Add/Update Mark", command=self.add_grade).pack(side=tk.LEFT, padx=2)
        ttk.Button(top_frame, text="Delete Subject", command=self.delete_subject).pack(side=tk.LEFT, padx=2)
        ttk.Button(top_frame, text="View Details", command=self.view_details).pack(side=tk.LEFT, padx=2)
        ttk.Button(top_frame, text="Delete Student", command=self.delete_student).pack(side=tk.LEFT, padx=2)
        ttk.Button(top_frame, text="Export CSV", command=self.export_csv).pack(side=tk.LEFT, padx=2)

        # --- Search Bar ---
        search_frame = ttk.Frame(self.root, padding=(10, 0, 10, 5))
        search_frame.pack(fill=tk.X)

        ttk.Label(search_frame, text="Search (ID/Name):").pack(side=tk.LEFT, padx=(0, 5))
        self.search_var = tk.StringVar()
        self.search_var.trace_add("write", lambda *args: self.refresh_table())
        ttk.Entry(search_frame, textvariable=self.search_var).pack(side=tk.LEFT, fill=tk.X, expand=True)

        # --- Treeview Table ---
        table_frame = ttk.Frame(self.root, padding=10)
        table_frame.pack(fill=tk.BOTH, expand=True)

        columns = ("ID", "Name", "Average", "Grade", "GPA")
        self.tree = ttk.Treeview(table_frame, columns=columns, show="headings")

        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor=tk.CENTER, width=130)

        scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.refresh_table()

    def refresh_table(self) -> None:
        """Refresh the displayed list of students based on search input."""
        for item in self.tree.get_children():
            self.tree.delete(item)

        query = self.search_var.get().lower().strip()

        for st in self.students.values():
            if query and (query not in st.student_id.lower() and query not in st.name.lower()):
                continue

            avg = grade.calculate_average(st.marks)
            letter = grade.get_letter_grade(avg)
            gpa_val = grade.get_gpa(avg)

            self.tree.insert("", tk.END, iid=st.student_id, values=(
                st.student_id, st.name, f"{avg:.2f}", letter, f"{gpa_val:.1f}"
            ))

    def add_student(self) -> None:
        """Prompt user to add a new student record."""
        sid = simpledialog.askstring("Add Student", "Enter Student ID:")
        if not sid:
            return
        sid = sid.strip()
        if sid in self.students:
            messagebox.showerror("Error", "Student ID already exists!")
            return

        name = simpledialog.askstring("Add Student", "Enter Student Name:")
        if not name:
            return

        self.students[sid] = Student(student_id=sid, name=name.strip())
        save_students(self.students)
        self.refresh_table()

    def edit_student(self) -> None:
        """Allow updating the name of the selected student."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a student from the table first!")
            return
        sid = selected[0]
        st = self.students[sid]

        new_name = simpledialog.askstring("Edit Name", f"Updating name for ID '{sid}':", initialvalue=st.name)
        if new_name and new_name.strip():
            st.name = new_name.strip()
            save_students(self.students)
            self.refresh_table()

    def add_grade(self) -> None:
        """Add or update a mark for the selected student with overwrite validation."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a student from the table first!")
            return
        sid = selected[0]
        st = self.students[sid]

        subject = simpledialog.askstring("Add Grade", "Enter Subject Name:")
        if not subject:
            return
        subject = subject.strip()

        # Check for existing subject (duplicate validation)
        if subject in st.marks:
            old_score = st.marks[subject]
            confirm = messagebox.askyesno(
                "Overwrite Subject",
                f"'{subject}' already exists with score {old_score}.\nDo you want to overwrite it?"
            )
            if not confirm:
                return

        try:
            score = float(simpledialog.askstring("Add Grade", f"Enter score for {subject} (0-100):"))
            if 0 <= score <= 100:
                st.add_or_update_mark(subject, score)
                save_students(self.students)
                self.refresh_table()
            else:
                messagebox.showerror("Error", "Score must be between 0 and 100.")
        except (ValueError, TypeError):
            messagebox.showerror("Error", "Invalid numerical score!")

    def delete_subject(self) -> None:
        """Prompt user to remove a specific subject mark from the selected student."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a student from the table first!")
            return
        sid = selected[0]
        st = self.students[sid]

        if not st.marks:
            messagebox.showinfo("Info", f"Student '{st.name}' has no subjects recorded.")
            return

        subject = simpledialog.askstring("Delete Subject", f"Enter subject to delete for {st.name}:")
        if not subject:
            return

        subject = subject.strip()
        if st.remove_mark(subject):
            save_students(self.students)
            self.refresh_table()
            messagebox.showinfo("Success", f"Removed '{subject}' from {st.name}.")
        else:
            messagebox.showerror("Error", f"Subject '{subject}' not found!")

    def view_details(self) -> None:
        """Show full mark breakdown and calculations for selected student."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a student first!")
            return
        st = self.students[selected[0]]

        marks_summary = "\n".join([f"• {sub}: {sc}" for sub, sc in st.marks.items()]) or "No subjects recorded."
        avg = grade.calculate_average(st.marks)

        details = (
            f"ID: {st.student_id}\nName: {st.name}\n\n"
            f"--- Marks ---\n{marks_summary}\n\n"
            f"Average: {avg:.2f} | Grade: {grade.get_letter_grade(avg)} | GPA: {grade.get_gpa(avg):.1f}"
        )
        messagebox.showinfo("Student Details", details)

    def delete_student(self) -> None:
        """Permanently delete selected student record."""
        selected = self.tree.selection()
        if not selected:
            messagebox.showwarning("Warning", "Select a student first!")
            return
        sid = selected[0]
        st = self.students[sid]

        if messagebox.askyesno("Confirm Delete", f"Delete student '{st.name}' ({sid})?"):
            del self.students[sid]
            save_students(self.students)
            self.refresh_table()

    def export_csv(self) -> None:
        """Export student table data to a CSV spreadsheet file."""
        if not self.students:
            messagebox.showwarning("Warning", "No records available to export!")
            return
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
        if path:
            export_to_csv(self.students, path)
            messagebox.showinfo("Success", f"Data exported successfully to:\n{path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentApp(root)
    root.mainloop()