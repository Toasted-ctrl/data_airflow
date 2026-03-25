import os
from dotenv import load_dotenv

class DiaConfig:
    print("Initializing Config: DIA")

    load_dotenv()

    db_protocol: str = os.getenv("DIA_DB_PROTOCOL")
    db_connection: str = os.getenv("DIA_DB_CONNECTION")
    
    db_hostname: str = os.getenv("DIA_DB_HOSTNAME")
    db_password: str = os.getenv("DIA_DB_PASSWORD")
    db_username: str = os.getenv("DIA_DB_USERNAME")
    db_database: str = os.getenv("DIA_DB_DATABASE")
    db_port: str = os.getenv("DIA_DB_PORT")

    api_key: str = os.getenv("DIA_API_KEY")

    @property
    def db_url(self):
        return f"{self.db_protocol}+{self.db_connection}://{self.db_username}:{self.db_password}@{self.db_hostname}:{self.db_port}/{self.db_database}"
    
    print("Initialized Config: DIA")

dia_config = DiaConfig()