# Ecommerce-Django

A fully-functional e-commerce application built with Django.

## Table of Contents

* Project Overview
* Features
* Tech Stack
* Getting Started

  * Prerequisites
  * Installation
  * Running the Project
* Configuration
* Folder Structure
* Usage
* Contributing
* License

## Project Overview

This project is a complete e-commerce application built using the Django framework. It offers features like user registration & login, product listings, shopping cart, order checkout, and more — all packaged in a clean, maintainable codebase.

## Features

* User authentication (sign up, login, logout)
* Email verification / account activation
* Product browsing and search
* Shopping cart and checkout
* Admin interface for product and order management
* Responsive frontend with template-based design
* Static files management (CSS/JS/images)
* Modular Django apps: `accounts`, `products`, `home`, etc.

## Tech Stack

* Backend: Python, Django
* Database: SQLite (default)
* Frontend: HTML, CSS, JavaScript
* Other: Django’s templating engine, Django admin, static files

## Getting Started

### Prerequisites

* Python 3.x installed
* pip (Python package installer)
* Virtual environment tool (venv, virtualenv) recommended

### Installation

1. Clone the repository

```bash
git clone https://github.com/shishir085/Ecommerce-Django.git
cd Ecommerce-Django
```

2. Create and activate a virtual environment

```bash
python3 -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

### Running the Project

1. Apply database migrations

```bash
python manage.py migrate
```

2. Create a superuser (for Django admin)

```bash
python manage.py createsuperuser
```

3. Run the development server

```bash
python manage.py runserver
```

4. Open your browser and navigate to `http://127.0.0.1:8000/`

## Configuration

* In `ecomm/settings.py` (or your settings module), configure email for account activation:

```python
EMAIL_HOST = 'smtp.your-email.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'your-email@example.com'
EMAIL_HOST_PASSWORD = 'your-password'
EMAIL_USE_TLS = True
```

* Adjust `ALLOWED_HOSTS`, `DEBUG`, and database settings as needed.
* If your project folder name differs (e.g., `ecomm` instead of `ecommerce`), ensure `DJANGO_SETTINGS_MODULE` in `manage.py` and `wsgi.py` matches.

## Folder Structure

```
Ecommerce-Django/
├─ accounts/        # Django app for user accounts & authentication
├─ products/        # Django app for product listing & management
├─ home/            # Django app for homepage, landing pages
├─ ecomm/           # Main project folder (contains settings, urls, wsgi)
├─ public/static/   # Static assets (CSS/JS/images)
├─ templates/       # Global templates shared among apps
├─ manage.py
└─ db.sqlite3       # Default database
```

## Usage

* Visit the homepage and browse products.
* Register a new user account; activate via email if configured.
* Login, add items to cart, and checkout.
* Admin users can log into Django Admin (`/admin`) to manage products, orders, and users.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/YourFeature`)
3. Make changes & commit them
4. Push to your fork and open a Pull Request

Please follow standard commit conventions and ensure new features are documented and tested.

## License

This project is open-source under the [MIT License](LICENSE).

---

