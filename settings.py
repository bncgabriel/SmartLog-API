import os
from dotenv import load_dotenv

load_dotenv()

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "1001")
DB_NAME = os.getenv("DB_NAME", "smartlog")
DB_USER = os.getenv("DB_USER", "smartlog_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "smartlog_password")

DATABASE_URL = os.getenv("DATABASE_URL") or (
    f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
