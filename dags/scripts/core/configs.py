import os
from dotenv import load_dotenv

class DiaConfig:
    print(" --- Initializing config ---")

    load_dotenv()

    dia_db_protocol: str = os.getenv("DIA_DB_PROTOCOL")
    dia_db_connection: str = os.getenv("DIA_DB_CONNECTION")
    
    dia_db_hostname: str = os.getenv("DIA_DB_HOSTNAME")
    dia_db_password: str = os.getenv("DIA_DB_PASSWORD")
    dia_db_username: str = os.getenv("DIA_DB_USERNAME")
    dia_db_database: str = os.getenv("DIA_DB_DATABASE")
    dia_db_port: str = os.getenv("DIA_DB_PORT")

    dia_api_key: str = os.getenv("DIA_API_KEY")

    @property
    def dia_db_url(self):
        return f"{self.dia_db_protocol}+{self.dia_db_connection}://{self.dia_db_username}:{self.dia_db_password}@{self.dia_db_hostname}:{self.dia_db_port}/{self.dia_db_database}"
    
    print("> Config initialized")

dia_config = DiaConfig()