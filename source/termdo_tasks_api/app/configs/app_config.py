import os


class AppConfig:
    HOST_NAME: str = os.uname().nodename
    PORT: int

    @classmethod
    def load(cls) -> None:
        cls.PORT = int(os.environ["APP_PORT"])
