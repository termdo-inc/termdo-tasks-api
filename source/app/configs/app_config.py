import os


class AppConfig:
    HOST: str = os.uname().nodename
    PORT: int = int(os.getenv("APP_PORT", "3002"))
