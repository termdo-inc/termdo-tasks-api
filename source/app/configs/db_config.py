import os


class DbConfig:
    HOST: str = os.getenv("POSTGRES_HOST", "localhost")
    PORT: int = int(os.getenv("POSTGRES_PORT", 5432))
    USER: str = os.getenv("POSTGRES_USER", "termdo_admin")
    PASSWORD: str = os.getenv("POSTGRES_PASSWORD", "termdo_password")
    DATABASE: str = os.getenv("POSTGRES_DB", "termdo_db")
