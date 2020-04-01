import os


class Configuration:
    """Takagi Configuration File"""

    def __init__(self):
        # MongoDB Configuration
        self.MONGO_ADDRESS = os.environ.get("MONGO_ADDRESS") or "127.0.0.1"
        self.MONGO_DATABASE = os.environ.get("MONGO_DATABASE") or "takagi"

        # Redis Configuration
        self.REDIS_ADDRESS = os.environ.get("REDIS_ADDRESS") or "127.0.0.1"

        # JWT Configuration
        self.JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY") or "DEV_SECRET"
        self.JWT_ACCESS_TOKEN_EXPIRES = 43200
