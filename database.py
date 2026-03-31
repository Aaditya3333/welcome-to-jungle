from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

print("=== DATABASE DEBUG START ===")
print(f"All env vars containing 'DATABASE': {[k for k in os.environ.keys() if 'DATABASE' in k]}")
DATABASE_URL = os.environ.get("DATABASE_URL")
print(f"DATABASE_URL found: {DATABASE_URL is not None}")
if DATABASE_URL:
    print(f"DATABASE_URL value: {DATABASE_URL}")
else:
    print("DATABASE_URL is None!")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()
print("=== DATABASE DEBUG END ===")