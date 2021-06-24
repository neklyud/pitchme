from betterconf import (
    field,
    Config,
)
from betterconf.caster import (
    to_bool,
    to_int,
)
import os
from dotenv import load_dotenv


class BaseConfig(Config):
    APP_TITTLE = field("APP_TITTLE", default="Events service")


class LocalConfig(BaseConfig):
    DEBUG = field("DEBUG", caster=to_bool, default=True)
    DB_USER = field("DB_USER", default="postgres")
    DB_PASSWORD = field("DB_PASSWORD", default="postgres")
    DB_HOST = field("DB_HOST", default="localhost")
    DB_PORT = field("DB_PORT", caster=to_int, default=5431)
    DB_NAME = field("DB_NAME", default="events")
    PATH_TO_MIGRATIONS = field(default="events/migrations/")
    DATABASE_DSN = "{driver}://{username}:{password}@{host}:{port}/{database}".format(
        driver="postgres",
        username=DB_USER.value,
        password=DB_PASSWORD.value,
        host=DB_HOST.value,
        port=DB_PORT.value,
        database=DB_NAME.value,
    )
    SQLALCHEMY_DATABASE_URI = "{driver}://{username}:{password}@{host}:{port}/{db}".format(
        driver="postgresql+asyncpg",
        username=DB_USER.value,
        password=DB_PASSWORD.value,
        host=DB_HOST.value,
        port=DB_PORT.value,
        db=DB_NAME.value,
    )


class ProdConfig(BaseConfig):
    pass


load_dotenv()

if os.environ['CONFIGURATION_TYPE'] == 'LOCAL':
    config = LocalConfig()
elif os.environ['CONFIGURATION_TYPE'] == 'PROD':
    config = ProdConfig()
else:
    raise EnvironmentError("Environment not set")
