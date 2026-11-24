# Django Blog API

A Blog Management REST API built with **Django** and **Django REST Framework**. This project provides blog CRUD operations with JWT Authentication and Role-Based Access Control.

## Features

- Custom User Model
- JWT Authentication
- Role-Based Permissions
- Author and Viewer Roles
- Create Blog Posts
- Retrieve All Blog Posts
- Retrieve Blog Details
- Update Blog Posts (PUT & PATCH)
- Delete Blog Posts
- UUID Primary Key
- Slug-Based Blog URLs
- Author Ownership Validation
- Swagger API Documentation

## Technologies Used

- Python
- Django
- Django REST Framework
- Simple JWT
- drf-yasg
- SQLite

## User Roles

| Role | Permissions |
|---|---|
| Author | Create, Read, Update and Delete own blog posts |
| Viewer | Read blog posts only |

## API Endpoints

| Method | Endpoint | Description | Access |
|---|---|---|---|
| GET | `/create_list/` | Get All Blogs | Author / Viewer |
| POST | `/create_list/` | Create Blog | Author |
| GET | `/update_delete/<slug>/` | Blog Details | Author / Viewer |
| PUT | `/update_delete/<slug>/` | Update Blog | Blog Owner |
| PATCH | `/update_delete/<slug>/` | Partial Update | Blog Owner |
| DELETE | `/update_delete/<slug>/` | Delete Blog | Blog Owner |
## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/django-blog-api.git
```

### 2. Go to Project Directory

```bash
cd django-blog-api
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Run Development Server

```bash
python manage.py runserver
```

## API Documentation

Swagger documentation:

```text
http://127.0.0.1:8000/swagger/
```

ReDoc documentation:

```text
http://127.0.0.1:8000/redoc/
```

## Authentication

This project uses JWT Authentication.

Include the access token in the request header:

```text
Authorization: Bearer <access_token>
```

## Project Structure

```text
django-blog-api/
│
├── accounts/
│   ├── models.py
│   ├── serializers.py
│   ├── permissions.py
│   ├── views.py
│   └── urls.py
│
├── blog/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
│
├── config/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt
```

## Future Improvements

- Blog Search and Filtering
- Pagination
- Blog Categories
- User Profile Management
- Automated API Testing

## Author

**Salim Reza**

GitHub: [Salim-raza](https://github.com/Salim-raza)

---

⭐ If you find this project useful, consider giving it a star!
