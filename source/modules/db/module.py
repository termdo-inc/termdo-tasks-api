from modules.db.core.db_handler import DbHandler


class DbModule:
    _instance: "DbModule | None" = None

    @staticmethod
    def instance() -> "DbModule":
        if DbModule._instance is None:
            DbModule._instance = DbModule()
        return DbModule._instance

    def __init__(self, handler: DbHandler = DbHandler()):
        self.handler = handler
        self.get_client = handler.get_client
