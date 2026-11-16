# Student Management System

A web-based Student Management System developed using Python and FastAPI to manage student records efficiently.

## Features

- Add new student records.
- View all registered students.
- View individual student details.
- Update existing student information.
- Delete student records.
- Store and manage student information using SQLite.
- Simple and user-friendly web interface.

## Technologies Used

- Python
- FastAPI
- SQLite
- HTML
- CSS
- JavaScript
- Jinja2 Templates

## Project Structure

```text
fa-project11/
│
├── templates/
│   ├── add-students.html
│   ├── edit_student.html
│   ├── home.html
│   └── single_std_details.html
│
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Setup

1. Clone the repository.

2. Install the required packages:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
uvicorn main:app --reload
```

4. Open your browser and visit:

```text
http://127.0.0.1:8000
```

## Learning Outcomes

- Developed REST API endpoints using FastAPI.
- Implemented CRUD operations.
- Connected a Python backend with an SQLite database.
- Integrated HTML templates with FastAPI.
- Practiced backend development and database management.

## Author

Vivek Vutkuri