from termdo_tasks_api.modules.db.core.db_handler import DbHandler


class DbModule:
    _instance: "DbModule | None" = None

    @staticmethod
    def get() -> "DbModule":
        if DbModule._instance is None:
            DbModule._instance = DbModule()
        return DbModule._instance

    def __init__(self):
        self._handler = DbHandler()
        self.create_pool = self._handler.create_pool
        self.get_connection = self._handler.get_connection
        self.close_pool = self._handler.close_pool
