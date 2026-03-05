# SafeSpot Backend (Django REST Framework)

## Structure

```
core/
├── config/              # Project configuration
│   ├── settings/        # Split settings (base, development, production)
│   ├── urls.py
│   └── wsgi.py
├── apps/
│   └── alerts/          # Alerts API app
├── manage.py
└── requirements.txt
```

## Setup

1. Copy `.env.example` to `.env` and set your values.

2. Create PostgreSQL database:
   ```bash
   createdb safespot
   ```

3. Install and run:
   ```bash
   cd core
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   ```


## Environment (.env)

| Variable | Description |
|----------|-------------|
| `DJANGO_SECRET_KEY` | Secret key (required in production) |
| `DJANGO_ENV` | `development` or `production` |
| `DATABASE_URL` | `postgresql://user:password@localhost:5432/safespot` |

## Run

```bash
# For mobile device testing, bind to all interfaces (0.0.0.0)
python manage.py runserver 0.0.0.0:8000
```

API: http://localhost:8000/api/alerts/

- **GET** `/api/alerts/?lat=33.57&lng=-7.59&radius=5` – list alerts near location
- **POST** `/api/alerts/` – create alert (JSON: `type`, `description`, `lat`, `lng`)

## Landing Page

The root URL (`/`) serves a marketing landing page with SEO, Privacy Policy, and Terms of Service.

- `/` – Landing page
- `/privacy/` – Privacy Policy (required for app stores)
- `/terms/` – Terms of Service
- `/robots.txt` – Sitemap
- `/sitemap.xml` – XML sitemap

Set `WEB_APP_URL` and `SITE_URL` in `.env` for production.

## Environment

- `DJANGO_ENV=development` (default) or `production`
- `DJANGO_SECRET_KEY` – required in production
