import os


class AppConfig:
    DEV: bool = False
    HOST: str = os.uname().nodename
    PORT: int = int(os.getenv("APP_PORT", "3002"))
