import os
from dotenv import load_dotenv

class Config:
    print(" --- Initializing config ---")

    load_dotenv()

    ingest_db_protocol: str = os.getenv("INGEST_DB_PROTOCOL")
    ingest_db_connection: str = os.getenv("INGEST_DB_CONNECTION")
    
    ingest_db_hostname: str = os.getenv("INGEST_DB_HOSTNAME")
    ingest_db_password: str = os.getenv("INGEST_DB_PASSWORD")
    ingest_db_username: str = os.getenv("INGEST_DB_USERNAME")
    ingest_db_database: str = os.getenv("INGEST_DB_DATABASE")
    ingest_db_port: str = os.getenv("INGEST_DB_PORT")

    @property
    def ingest_db_url(self):
        return f"{self.ingest_db_protocol}+{self.ingest_db_connection}://{self.ingest_db_username}:{self.ingest_db_password}@{self.ingest_db_hostname}:{self.ingest_db_port}/{self.ingest_db_database}"
    
    print("> Config initialized")

config = Config()