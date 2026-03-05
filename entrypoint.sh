#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "⏳ Waiting for PostGIS database to boot..."

# Loop until the database port is accepting connections
while ! nc -z db 5432; do
  sleep 0.5
done

echo "✅ PostGIS is online!"

# Apply the GeoDjango database migrations automatically
echo "📦 Applying database migrations..."
python manage.py migrate

# Collect static files (crucial so your Django Admin map renders correctly)
echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

# Execute the main command passed from docker-compose.yml (e.g., gunicorn or celery)
exec "$@"