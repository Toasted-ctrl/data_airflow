from airflow.sdk import task

from scripts.core.configs import dia_config

def dia_request_json(str=None):
    return f"DB url: {dia_config.api_key}"