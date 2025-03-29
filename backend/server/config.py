import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.app_name = os.getenv("APP_NAME", "test_rh_intuitive")
        self.db_user = os.getenv("DB_USER")
        self.db_password = os.getenv("DB_PASSWORD")
        self.db_host = os.getenv("DB_HOST", "localhost")
        self.db_name = os.getenv("DB_NAME")
        self.db_url = f"mysql+pymysql://{self.db_user}:{self.db_password}@{self.db_host}/{self.db_name}"
        self.api_version = "v1"
        self.host = os.getenv("HOST", "0.0.0.0")
        self.port = int(os.getenv("PORT", 8000))

settings = Settings()