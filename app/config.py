import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-key-123')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    LLM_TOKEN = os.getenv('LLM_TOKEN')
    MODEL_NAME = os.getenv('MODEL_NAME', 'gemini-1.5-flash')
    APP_PORT = int(os.getenv('APP_PORT', 5000))
    LLM_BASE_URL = os.getenv('LLM_BASE_URL', 'https://delcom.org/api')
    MODEL_NAME = os.getenv('MODEL_NAME', 'gemini-2.0-flash')