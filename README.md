# CareerConnect - Django Online Job Portal

CareerConnect is a professional Django job portal built with beginner-friendly code and recruiter-ready project structure. It supports posting jobs, browsing openings, applying for jobs, editing listings, deleting listings, and managing data through the Django admin.

## Features

- Django project architecture with a dedicated `jobs` app
- SQLite database for simple local setup
- `Job` and `Application` models
- Create, read, update, and delete job listings
- Candidate application form
- Django admin registration for jobs and applications
- Responsive templates with reusable `base.html`
- Static CSS and JavaScript organized under Django static folders
- Clean README, `.gitignore`, requirements, and AGPL-3.0 licensing

## Tech Stack

- Python 3.10+
- Django 5
- SQLite
- HTML, CSS, JavaScript

## Project Structure

```text
Online-job-portal/
├── job_portal/          # Django project settings and root URLs
├── jobs/                # Jobs app: models, forms, views, URLs, admin
├── templates/           # Shared and app templates
├── static/              # CSS and JavaScript assets
├── manage.py
├── requirements.txt
├── README.md
└── LICENSE
```

## Setup

1. Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Apply migrations:

```bash
python manage.py migrate
```

4. Create an admin user:

```bash
python manage.py createsuperuser
```

5. Run the development server:

```bash
python manage.py runserver
```

Open `http://127.0.0.1:8000/` in your browser.

## Main URLs

- `/` - Home page
- `/jobs/` - Browse and search jobs
- `/jobs/new/` - Post a new job
- `/jobs/<id>/edit/` - Edit a job
- `/jobs/<id>/delete/` - Delete a job
- `/jobs/<id>/apply/` - Apply for a job
- `/admin/` - Django admin

## Interview Notes

This project demonstrates core Django skills: project/app structure, ORM models, model forms, function-based views, templates, static files, URL routing, CRUD workflows, admin customization, migrations, and SQLite configuration.

## License

This project is licensed under the GNU Affero General Public License v3.0. See `LICENSE` for details.
