import os

from dotenv import load_dotenv

class RuneScapeConfig:
    print("Initializing Config: RuneScape")

    load_dotenv()

    db_protocol: str = os.getenv("RUNESCAPE_DB_PROTOCOL")
    db_connection: str = os.getenv("RUNESCAPE_DB_CONNECTION")
    db_hostname: str = os.getenv("RUNESCAPE_DB_HOSTNAME")
    db_password: str = os.getenv("RUNESCAPE_DB_PASSWORD")
    db_username: str = os.getenv("RUNESCAPE_DB_USERNAME")
    db_database: str = os.getenv("RUNESCAPE_DB_DATABASE")
    db_port: str = os.getenv("RUNESCAPE_DB_PORT")

    description_hiscores: str = "Runescape Player Hiscores"
    description_runemetrics: str = "Runescape Player Runemetrics Profile"

    @property
    def db_url(self) -> str:
        return f"{self.db_protocol}+{self.db_connection}://{self.db_username}:{self.db_password}@{self.db_hostname}:{self.db_port}/{self.db_database}"

runescape_config = RuneScapeConfig()