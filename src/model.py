from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, Integer, Float, Index,  ForeignKey, DateTime, Text, JSON, Boolean
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime, timezone
import os
from dotenv import load_dotenv

# configure database path
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./chatbot.db" 
)

engine = create_engine(
    DATABASE_URL,
    echo=False,
    connect_args={"check_same_thread": False} if "sqlite" in DATABASE_URL else {}
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = Session()
base = declarative_base

class Customer(base):
    __tablename__ = 'customer'

    id = Column(Integer,primary_key=True,Index=True)
    name = Column(String(100),nullable=True)
    Phone_no = Column(String(10),unique=True, Index=True)
    email = Column(String(100), nullable=True)
    created_at = Column(DateTime, default=datetime.now(timezone.utc))
    last_interacted_at = Column(DateTime, default=datetime.now(timezone.utc))