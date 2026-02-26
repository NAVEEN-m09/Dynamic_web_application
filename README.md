# Django 2nd

This project is a Django web app located inside `unit/`.

## Tech Used

- Python 3.11
- Django 5.2.x
- Django built-in authentication system (`django.contrib.auth`)
- Django messages framework (`django.contrib.messages`)
- SQLite database (`db.sqlite3`)
- HTML templates + static assets (Bootstrap/CSS/JS from `travellop/templates/assets`)

## Implemented Features

- User Registration page
- User Login page
- User Logout flow
- Auth links placed in home page navigation (`index.html`)
- Validation and flash messages for registration/login

## Auth Routes

Project routes include `accounts` app:

- `/accounts/register/` -> create account
- `/accounts/login/` -> sign in
- `/accounts/logout/` -> sign out

Main site home route:

- `/travellop/` -> index page

## Database

Configured database:

- Engine: `django.db.backends.sqlite3`
- File: `unit/db.sqlite3`
- Settings file: `unit/unit/settings.py`

User account data is stored in Django default auth tables, mainly:

- `auth_user`

## Where Main Auth Code Is

- `unit/accounts/views.py` -> `register`, `login_view`, `logout_view`
- `unit/accounts/urls.py` -> auth URL mappings
- `unit/accounts/templates/accounts/register.html`
- `unit/accounts/templates/accounts/login.html`
- `unit/travellop/templates/index.html` -> Login/Register/Logout nav links

## Run Locally

```bash
cd unit
python manage.py migrate
python manage.py runserver
```

Open:

- `http://127.0.0.1:8000/travellop/`
- `http://127.0.0.1:8000/accounts/register/`
- `http://127.0.0.1:8000/accounts/login/`

## Verification Done

- `python manage.py check` passes
- Registration saves user in DB
- Login authenticates and redirects to `/travellop/`
- Logout clears session and redirects to `/travellop/`
