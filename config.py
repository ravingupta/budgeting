import os
from sqlmodel import create_engine, SQLModel
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    SECRET: str = "secret"
    DEBUG: bool = True
    DB_URI: str = "sqlite:///DB/budgeting.db"
    connection: any = None

    def __init__(self):
        super().__init__()
        self.DB_URI = "sqlite:///" + os.environ.get('DB_DIR', 'DB/') + os.environ.get('DB_NAME', 'budgeting.db')
    

class DevelopmentConfig(Config):

    def __init__(self):
        super().__init__()
        self.connection = create_engine(self.DB_URI, connect_args = {"check_same_thread": False})
    

class ProductionConfig(Config):

    def __init__(self):
        super().__init__()
        self.DEBUG = False
        self.connection = create_engine(self.DB_URI, connect_args = {"check_same_thread": False})
    

# Load the configuration
FLASK_ENV = os.getenv("FLASK_ENV", "development")
appConfig = ProductionConfig() if FLASK_ENV == 'production' else DevelopmentConfig()
