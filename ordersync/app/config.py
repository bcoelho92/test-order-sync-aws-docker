import os
from dataclasses import dataclass

@dataclass
class Config:
    ENV: str = os.getenv("ENV","development")
    DEBUG: bool = ENV == "development"

    AWS_REGION: str = os.getenv("AWS_REGION", "us-east-1")
    DYNAMODB_TABLE: str = os.getenv("DYNAMODB_TABLE", "orders")
    SQS_QUEUE_URL: str = os.getenv("SQS_QUEUE_URL", "")

    EXTERNAL_API_URL: str = os.getenv("EXTERNAL_API_URL", "https://example.com/payments")

def load_config() -> Config:
    return Config()