# Deploy SafeSpot to OVH

## Prerequisites

- Docker and Docker Compose installed on your OVH VPS
- Domain or IP pointing to your server

## 1. Clone and configure

```bash
cd /opt  # or your preferred directory
git clone <your-repo-url> SafeSpot
cd SafeSpot/core
```

## 2. Create production .env

```bash
cp .env.prod.example .env
nano .env  # Edit with your values
```

Required variables:
- `POSTGRES_PASSWORD` – Strong password for PostgreSQL
- `DJANGO_SECRET_KEY` – Generate with `python -c "import secrets; print(secrets.token_urlsafe(50))"`
- `DJANGO_ALLOWED_HOSTS` – Comma-separated: `yourdomain.com,www.yourdomain.com,your-server-ip`
- `CORS_ALLOWED_ORIGINS` – Comma-separated: `https://yourdomain.com,https://www.yourdomain.com`

## 3. Build and run

```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build
```

## 4. Create superuser (first time only)

```bash
docker-compose -f docker-compose.yml -f docker-compose.prod.yml exec web python manage.py createsuperuser
```

## 5. Expose port 8000

- OVH VPS: Open port 8000 in the firewall
- Or put Nginx/Caddy in front as reverse proxy (recommended for HTTPS)

## Useful commands

```bash
# View logs
docker-compose -f docker-compose.yml -f docker-compose.prod.yml logs -f web

# Restart after code changes
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d --build web

# Stop
docker-compose -f docker-compose.yml -f docker-compose.prod.yml down
```
