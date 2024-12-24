
# PaperLessExam

PaperLessExam is a web application designed to reduce paper consumption in academic institutions by digitizing the question paper management process. It simplifies the workflow for faculty and students by offering a secure, eco-friendly, and efficient way to handle question papers.

# Features
Admin Dashboard:
Manage users, subjects, and access permissions. 

Role-Based Access:
- Admin: Manage all activities.
- Faculty: Upload and manage question papers.
- Students: Access uploaded question papers based on courses.

Secure Storage: Ensures uploaded question papers are encrypted and accessible only to authorized users.

# Technologies Used
Backend: Django (Python), REST Framework (if APIs are used)

Frontend: HTML5, CSS3, JavaScript (Bootstrap or React for enhanced UI)

Database: SQLite (Development), PostgreSQL/MySQL (Production)

Authentication: Django Authentication System with role-based access control


## Installation

Clone the Repository:

```bash
    git clone https://github.com/yourusername/PaperLessExam.git
    cd PaperLessExam
```
Create and Activate a Virtual Environment:
```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate     # Windows
```
Install Dependencies:
```bash
    pip install -r requirements.txt
```
Apply Migrations:
```bash
    python manage.py makemigrations
    python manage.py migrate
```
Run the Development Server:
```bash
    python manage.py runserver
```


## Acknowledgements

 - Inspired by the need for sustainability in education.
 - Thanks to the Django and open-source communities for their tools and frameworks.
