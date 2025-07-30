from dataclasses import dataclass
from datetime import datetime

from asyncpg import Record


@dataclass
class TaskModel:
    task_id: int
    account_id: int
    title: str
    description: str
    is_completed: bool
    created_at: datetime
    updated_at: datetime

    @staticmethod
    def is_valid_model(record: Record) -> bool:
        return (
            isinstance(record.get("task_id"), int)
            and isinstance(record.get("account_id"), int)
            and isinstance(record.get("title"), str)
            and isinstance(record.get("description"), str)
            and isinstance(record.get("is_completed"), bool)
            and isinstance(record.get("created_at"), datetime)
            and isinstance(record.get("updated_at"), datetime)
        )

    @staticmethod
    def from_record(record: Record) -> "TaskModel":
        if not TaskModel.is_valid_model(record):
            raise ValueError("Invalid record format for TaskModel")

        return TaskModel(
            task_id=record["task_id"],
            account_id=record["account_id"],
            title=record["title"],
            description=record["description"],
            is_completed=record["is_completed"],
            created_at=record["created_at"],
            updated_at=record["updated_at"],
        )

    @staticmethod
    def from_records(records: list[Record]) -> list["TaskModel"]:
        return [TaskModel.from_record(record) for record in records]
