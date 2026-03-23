import os

from airflow.sdk import task
from dotenv import load_dotenv

@task
def request_json():
    print("Hello from this function")