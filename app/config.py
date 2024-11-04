import boto3
from dataclasses import dataclass
from os import getenv
from dotenv import load_dotenv

load_dotenv()

@dataclass
class AWSSession:
    access_key: str = getenv('AWS_ACCESS_KEY_ID')
    secret_key: str = getenv('AWS_SECRET_ACCESS_KEY')

@dataclass
class AWSConfig:
    service_name: str
    endpoint_url: str
    region_name: str = getenv('AWS_DEFAULT_REGION')

db_config = AWSConfig(service_name='dynamodb', endpoint_url=getenv('ENDPOINT_DB'))

@dataclass
class DatabaseConfig:
    endpoint: str
    region_name: str
    key_id: str
    access_key: str


@dataclass
class DBPhysConfig:
    endpoint_url: str = getenv('ENDPOINT_PHYS')
    region_name: str = getenv('REGION_NAME')
    aws_access_key_id: str = getenv('AWS_ACCESS_KEY_ID')
    aws_secret_access_key: str = getenv('AWS_SECRET_ACCESS_KEY')

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