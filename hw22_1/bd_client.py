import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import logging

load_dotenv()

logging.basicConfig(level=logging.INFO)

class SQLAlchemyClient:
    def __init__(self):
        self.db_url = os.getenv("bd_url")
        if not self.db_url:
            raise ValueError(f"{db_url} is not set in the .env file.")
        self.engine = create_engine(self.db_url)
        self.Session = sessionmaker(bind=self.engine)

    def get_session(self):
        return self.Session()

    def create_tables(self, base_model):
        base_model.metadata.create_all(self.engine)
