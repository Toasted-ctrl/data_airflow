from airflow.sdk import task

from scripts.core.configs import dia_config

def dia_request_json(request_data: dict):
    return f"DB url: {dia_config.api_key}"