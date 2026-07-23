# 🎓 Student Grade Management System

<img width="876" height="546" alt="image" src="https://github.com/user-attachments/assets/6dab0e5f-cb57-4e9b-a4f2-bb8d8bf497d9" />

A desktop application built with **Python** and **Tkinter** for managing student records, subject marks, grades, and GPA. The project follows a **modular architecture**, separating the user interface, business logic, data model, and file handling into independent modules for better readability and maintainability.

This project was developed to practice **Object-Oriented Programming (OOP)**, **GUI development**, **file handling**, and **clean software design** while creating a practical application that demonstrates CRUD operations and data persistence.

---

## ✨ Features

### Student Management
- Add new students
- Edit student names
- Delete student records
- Search students by ID or name
- Prevent duplicate Student IDs

### Grade Management
- Add subject marks
- Update existing marks
- Delete individual subjects
- Automatic average calculation
- Automatic GPA calculation
- Automatic letter grade calculation

### Data Management
- Save records using text file handling
- Automatically load saved records on startup
- Export all student records to CSV format

### Validation & Error Handling
- Score validation (0–100)
- Duplicate subject confirmation
- Invalid input handling
- Confirmation before deleting records
- Graceful error messages
<img width="874" height="104" alt="image" src="https://github.com/user-attachments/assets/7029f3b3-0a2e-4183-ae88-685397ffa7e7" />

---

## 📂 Project Structure

```text
Student-Grade-Management-System/
│
├── main.py
├── student.py
├── grade.py
├── file_handler.py
├── students.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## 🏗 Project Architecture

```
                User
                  │
                  ▼
          Student Management GUI
              (Tkinter UI)
                  │
        ┌─────────┼─────────┐
        │         │         │
        ▼         ▼         ▼
  Student.py   Grade.py  File_Handler.py
        │         │         │
        └─────────┼─────────┘
                  │
                  ▼
            students.txt
```

---

## 🛠 Technologies Used

- Python 3
- Tkinter
- Object-Oriented Programming (OOP)
- Dataclasses
- File Handling
- CSV Module
- Type Hints

---

## 🎯 Learning Objectives

This project was built to strengthen practical knowledge of:

- Python Programming
- Object-Oriented Programming
- GUI Development with Tkinter
- Modular Programming
- File Handling
- CRUD Operations
- CSV Export
- Error Handling
- Type Hinting
- Software Architecture

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/sakshyampudasaini/Student-Grade-Management-System.git
```

### Navigate to the project

```bash
cd Student-Grade-Management-System
```

### Run the application

```bash
python main.py
```

No third-party libraries are required.

---

## 📌 Why This Project?

Most beginner Python calculator or management projects place all functionality into a single file, making them difficult to maintain and extend.

This project demonstrates a cleaner approach by separating the application into dedicated modules for the user interface, student model, grading logic, and file handling. The result is a codebase that is easier to understand, modify, and scale as new features are added.

---

## 🔮 Future Improvements

- SQLite database integration
- User authentication system
- Attendance management
- Report card generation
- PDF export
- Student ranking system
- Charts and statistics
- Dark/Light theme
- Automatic backup and restore

---

## 🤝 Contributing

Contributions, suggestions, and feature requests are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License**.

---

## 👨‍💻 Author

**Sakshyam Pudasaini**

GitHub: https://github.com/sakshyampudasaini

---

⭐ If you found this project useful, consider giving it a star.
