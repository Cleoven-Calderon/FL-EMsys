# EMsys - Employee Management System

A Flask-based web application for managing employees, teams, and team communications.

## Overview

EMsys is a CRUD application that allows administrators to manage employee records and assign them to teams. Employees can log in to view their team dashboard, see announcements, and view their coworkers.

## Screenshots
<img width="1919" height="1079" alt="Screenshot 2026-02-13 203740" src="https://github.com/user-attachments/assets/f770ed20-e2ba-4db2-8c85-1dd49358d563" />
<img width="1919" height="1079" alt="Screenshot 2026-02-13 203804" src="https://github.com/user-attachments/assets/1d3a6576-2a27-41a3-b78f-03c180a2c97f" />
<img width="1919" height="1079" alt="Screenshot 2026-02-13 203855" src="https://github.com/user-attachments/assets/6883501b-1b5c-42e1-a4d9-f58a16aa3fd2" />


## Features

### Admin Features
- Secure login with username and password
- Add new employees with ID, name, and team assignment
- Update employee information (name, team)
- Delete employees from the system
- Post announcements and tasks to team bulletin boards
- View all employees in a sortable table

### Employee Features
- Login using employee ID
- View team-specific dashboard
- Access team bulletin board with tasks and announcements
- See list of team members with contact information
- Persistent sessions across page refreshes

## Team Structure

The system supports three teams:
- Creative Team
- Sound Team
- Technical Team

## Technology Stack

- Backend: Flask (Python)
- Frontend: HTML, CSS, Jinja2 templates
- Data Storage: In-memory (Python lists and dictionaries)
- Session Management: Flask sessions

## Installation

1. Clone or download the project

2. Create a virtual environment:
```bash
python -m venv env
```

3. Activate the virtual environment:
- Windows: `env\Scripts\activate`
- Mac/Linux: `source env/bin/activate`

4. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Ensure virtual environment is activated

2. Run the Flask application:
```bash
python app.py
```

3. Open browser and navigate to:
```
http://127.0.0.1:5000
```

4. To stop the server, press `Ctrl+C` in the terminal

## Default Credentials

### Admin Login
- Username: `admin`
- Password: `admin123`

### Employee Login
Employees must first be added by an admin. Use the assigned Employee ID to log in.

## Project Structure
```
EMSYS/
├── app.py                      # Main Flask application with routes
├── models.py                   # Data models and CRUD functions
├── requirements.txt            # Python dependencies
├── templates/
│   ├── index.html             # Landing page
│   ├── admin/
│   │   ├── admin_verify.html  # Admin login page
│   │   └── admin_panel.html   # Admin dashboard
│   └── user/
│       ├── user_verify.html   # Employee login page
│       ├── creative_team.html # Creative team dashboard
│       ├── sound_team.html    # Sound team dashboard
│       └── technical_team.html# Technical team dashboard
└── static/
    └── css/
        └── style.css          # Application styling
```

## Usage Guide

### For Administrators

1. Navigate to home page and click "Admin Login"
2. Enter admin credentials
3. Use "Add New Employee" form to create employee records
4. Click "Edit" to modify employee information
5. Click "Delete" to remove employees
6. Use "Add Bulletin Board Item" to post team announcements
7. Click "Logout" when finished

### For Employees

1. Navigate to home page and click "Employee Login"
2. Enter your Employee ID (provided by admin)
3. View your team bulletin board for tasks and announcements
4. See your team members in the "Your Team Members" section
5. Click "Logout" when finished

## Data Persistence

This application uses in-memory storage. All data (employees, bulletin items) will be lost when the server restarts. This is suitable for development and demonstration purposes.

For production use, integrate a database system (SQLite, PostgreSQL, MySQL).

## Security Notes

This is an educational project with basic security:
- Admin password is hardcoded
- No employee passwords (ID-only verification)
- Sessions are used for authentication
- Data is not encrypted

Not suitable for production use without additional security measures.

## File Descriptions

### app.py
Contains all Flask routes and application logic. Handles admin and user authentication, employee management, and bulletin board operations.

### models.py
Defines data structures and provides CRUD functions for employees and bulletin items. Contains in-memory storage using Python lists and dictionaries.

### templates/
HTML templates using Jinja2 syntax for dynamic content rendering. Includes separate pages for admin and employee interfaces.

### static/css/style.css
Complete styling for the application using a black and white color scheme with gray accents.

## License

This is a school project created for educational purposes.
