import os


class BaseConfig:
    JSON_SORT_KEYS = False
    CORS_ORIGINS = "*"
    RATELIMIT_DEFAULT = "100 per minute"


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


def get_config():
    env = os.getenv("FLASK_ENV", "development")
    if env == "production":
        return ProductionConfig
    return DevelopmentConfig
