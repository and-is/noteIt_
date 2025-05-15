from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

APP_NAME = os.getenv('APP_NAME', 'noteit')
ENV = os.getenv('ENV', 'development')
DEBUG = os.getenv('DEBUG', 'FALSE') == 'TRUE'
SECRET_KEY = os.getenv('SECRET_KEY')
DATABASE_URL = os.getenv('DATABASE_URL')
PORT = int(os.getenv('PORT', 8000))