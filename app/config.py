from boto_orm.models.config import AWSConfig, BaseConfig, AWSSession
from pydantic_settings import SettingsConfigDict

class ProfileConfig(BaseConfig):
    session: AWSSession
    phys_db: AWSConfig
    termex_db: AWSConfig
    s3_config: AWSConfig

    model_config = SettingsConfigDict(yaml_file='boto.yaml')

configure = ProfileConfig()
