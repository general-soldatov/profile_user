import boto3
from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv

@dataclass
class DatabaseConfig:
    endpoint: str
    region_name: str
    key_id: str
    access_key: str

load_dotenv()

database_config = DatabaseConfig(endpoint=getenv('ENDPOINT'),
                                 region_name=getenv('REGION_NAME'),
                                 key_id=getenv('AWS_ACCESS_KEY_ID'),
                                 access_key=getenv('AWS_SECRET_ACCESS_KEY'))

dynamodb_config = boto3.resource(
                'dynamodb',
                endpoint_url=database_config.endpoint,
                region_name=database_config.region_name,
                aws_access_key_id=database_config.key_id,
                aws_secret_access_key=database_config.access_key
                )