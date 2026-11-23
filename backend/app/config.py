import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)
DATA_DIR = os.path.join(PROJECT_DIR, "data")
DB_PATH = os.path.join(DATA_DIR, "app.db")
SESSION_DURATION_DAYS = 7
SECRET_KEY = "dev-secret-key-change-in-production"
