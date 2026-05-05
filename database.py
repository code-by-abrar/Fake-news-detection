import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Docker-compose mein jo URL diya tha, wahi yahan use hoga
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://myuser:mypassword@db:5432/fakenewsdb")

engine = create_engine(DATABASE_URL,connect_args={"sslmode": "require"} if "neon.tech" in DATABASE_URL else {})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Database session manage karne ke liye function
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()