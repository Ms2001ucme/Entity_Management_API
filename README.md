# Entity Management API

A modular backend API built using **Django** and **Django REST Framework** to manage entities such as Vendors, Products, Courses, and Certifications with flexible mapping between them.

## Tech Stack

- Python
- Django
- Django REST Framework
- drf-yasg (Swagger API documentation)
- SQLite (development database)

---

## Features

- Vendor management
- Product management
- Course management
- Certification management
- Vendor–Product mapping
- Product–Course mapping
- Course–Certification mapping
- RESTful APIs
- Swagger API documentation

---

## API Documentation

Interactive API documentation is available using Swagger.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Ms2001ucme/Entity_Management_API.git
cd Entity_Management_API

**Create a virtual environment**
- python -m venv venv

**Install Dependencies**
- pip install -r requirements.txt

**Apply Migrations**
- python manage.py migrate

**Start Server**
- python manage.py runserver
