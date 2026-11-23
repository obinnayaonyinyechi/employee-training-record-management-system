# Employee Training Record Management System

A Django-based web application for managing employee training records. The application provides a dashboard for monitoring training activities, CRUD functionality, search, filtering, and a Django administration interface.

## Features

- Dashboard with training statistics
- Create, read, update and delete training records
- Search by employee name and training title
- Filter by training status
- Training date management
- Training duration validation
- Django administration interface
- Responsive user interface
- SQLite database for local development

## Technologies Used

- Python
- Django 5.2
- SQLite
- HTML5
- CSS3
- Git
- GitHub

## Training Record Fields

- Training Title
- Employee Name
- Training Date
- Training Duration (Hours)
- Training Status

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/employee-training-record-management-system.git
```

### 2. Enter the project directory

```bash
cd employee-training-record-management-system
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run database migrations

```bash
python manage.py migrate
```

### 7. Create an administrator account

```bash
python manage.py createsuperuser
```

### 8. Start the development server

```bash
python manage.py runserver
```

### 9. Open the application

Dashboard:

http://127.0.0.1:8000/

Admin:

http://127.0.0.1:8000/admin/

## Testing

Run the automated tests:

```bash
python manage.py test
```

## Project Structure

```text
employee_training_system/
├── employee_training_system/
├── training/
├── templates/
├── static/
├── manage.py
├── requirements.txt
└── README.md
```

## Author

Developed as a practical Python and Django project for employee training record management.

## License

This project is a practical assessment.
