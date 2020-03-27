import os


class Configuration:
    """Takagi Configuration File"""

    def __init__(self):
        # MongoDB Configuration
        self.MONGO_ADDRESS = os.environ.get("MONGO_ADDRESS") or "10.0.0.1"
        self.MONGO_DATABASE = os.environ.get("MONGO_DATABASE") or "takagi"

        # JWT Configuration
        self.JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY") or "DEV_SECRET"
        self.JWT_ACCESS_TOKEN_EXPIRES = 43200