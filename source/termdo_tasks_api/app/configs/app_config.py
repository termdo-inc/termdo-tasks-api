import os


class AppConfig:
    HOSTNAME: str
    PORT: int

    @classmethod
    def load(cls) -> None:
        cls.HOSTNAME = os.uname().nodename
        cls.PORT = int(os.environ["APP_PORT"])
