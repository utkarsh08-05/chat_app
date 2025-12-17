Railway deployment notes

1) Create a Railway project and link this repo.

2) Add environment variables in Railway:
   - `SECRET_KEY` (your Django secret)
   - `DEBUG` (set to `False`)
   - `DATABASE_URL` (Railway Postgres will provide)
   - `ALLOWED_HOSTS` (comma-separated, e.g. `your-app.up.railway.app`)
   - optional: `CSRF_TRUSTED_ORIGINS` (comma-separated, include https:// domains)

3) Build & start commands (Railway):
   - Build Command: `pip install -r requirements.txt && python manage.py migrate && python manage.py collectstatic --noinput`
   - Start Command: `gunicorn vartalap.wsgi --log-file -`

4) Notes:
   - `DATABASES` is configured to use `DATABASE_URL` via `dj-database-url`.
   - Static files are served using WhiteNoise and `STATICFILES_STORAGE`.
   - Ensure `psycopg2-binary`, `dj-database-url`, and `gunicorn` are present in `requirements.txt` (they are).

5) After deploy: run migrations if not run during build:
   - `railway run python manage.py migrate`

