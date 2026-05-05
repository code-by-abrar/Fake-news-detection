from sqlalchemy import Column, Integer, String, Boolean, Float
from database import Base

class NewsRecord(Base):
    __tablename__ = "news_records"

    id = Column(Integer, primary_key=True, index=True)
    news_content = Column(String)  # User ka bheja hua text
    prediction = Column(String)    # "Fake" ya "Real"
    confidence = Column(Float)     # AI kitna sure hai (e.g. 0.98)