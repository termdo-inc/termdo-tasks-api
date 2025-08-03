import os


class DbConfig:
    HOST: str
    PORT: int
    USER: str
    PASSWORD: str
    NAME: str

    @classmethod
    def load(cls) -> None:
        cls.HOST = os.environ["DB_HOST"]
        cls.PORT = int(os.environ["DB_PORT"])
        cls.USER = os.environ["DB_USER"]
        cls.PASSWORD = os.environ["DB_PASSWORD"]
        cls.NAME = os.environ["DB_NAME"]
