from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

APP_NAME = os.getenv('APP_NAME', 'noteit')
ENV = os.getenv('ENV', 'development')
DEBUG = os.getenv('DEBUG', 'FALSE') == 'TRUE'
SECRET_KEY = os.getenv('SECRET_KEY')

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT', '3306')
DB_NAME = os.getenv('DB_NAME')

#DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
print(DATABASE_URL)

PORT = int(os.getenv("PORT", 8000))
