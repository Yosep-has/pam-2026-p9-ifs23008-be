from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.config import Config
from flask_sqlalchemy import SQLAlchemy

# Inisialisasi db di sini
db = SQLAlchemy()
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()