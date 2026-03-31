from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

print("=== DATABASE DEBUG START ===")
print(f"All env vars containing 'DATABASE': {[k for k in os.environ.keys() if 'DATABASE' in k]}")
# Try environment variable first, then fallback to hardcoded Render URL
DATABASE_URL = os.environ.get("DATABASE_URL")

if not DATABASE_URL:
    print("DATABASE_URL not found in environment, using hardcoded Render URL")
    # Replace this with your actual Render database internal URL
    DATABASE_URL = "postgresql://magix_user:e44v5X95q67YRl9tAC7StaAxLudmbY6x@dpg-d75oismuk2gs73dd4v60-a/magix"
    print(f"Using DATABASE_URL: {DATABASE_URL}")
else:
    print(f"DATABASE_URL value: {DATABASE_URL}")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
print("=== DATABASE DEBUG END ===")