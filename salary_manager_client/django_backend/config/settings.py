from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# GANTI dengan nilai yang aman di production!
SECRET_KEY = "django-insecure-ganti-ini-di-production-dengan-value-yang-aman"

DEBUG = True
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "corsheaders",
    "salary_app",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "config.urls"

# Izinkan semua origin (Vue dev server)
CORS_ALLOW_ALL_ORIGINS = True

# URL FastAPI yang sedang berjalan
FASTAPI_BASE_URL = "http://127.0.0.1:8000"
