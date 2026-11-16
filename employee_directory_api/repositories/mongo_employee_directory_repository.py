from datetime import datetime, timezone
from typing import Collection, Optional, List
from uuid import UUID

from pymongo import ReturnDocument

from models import employee_directory


from models.employee_directory import EmployeeDirectory
from repositories.employee_directory_repository import EmployeeDirectoryRepository


class MongoEmployeeDirectoryRepository(EmployeeDirectoryRepository):

    def __init__(self, collection: Collection):
        self._collection = collection


    def add(self, employee_directory: EmployeeDirectory) -> EmployeeDirectory:
        self._collection.insert_one(self._to_document(employee_directory))
        return employee_directory


    def get(self, employee_id: UUID) -> Optional[EmployeeDirectory]:
        document = self._collection.find_one({"_id": str(employee_id)})
        return self._to_entity(document) if document else None


    def list(self) -> List[EmployeeDirectory]:
        return [self._to_entity(doc) for doc in self._collection.find()]


    def update(self, employee_id: UUID, data: dict) -> Optional[EmployeeDirectory]:
        data["updated_at"] = datetime.now(timezone.utc)
        document = self._collection.find_one_and_update(
            {"_id": str(employee_id)},
            {"$set": data},
            return_document=ReturnDocument.AFTER,
    )
        return self._to_entity(document) if document else None


    def delete(self, employee_id: UUID) -> bool:
        result = self._collection.delete_one({"_id": str(employee_id)})
        return result.deleted_count == 1


    @staticmethod
    def _to_document(todo: EmployeeDirectory) -> dict:
        document = employee_directory.model_dump()
        document["_id"] = str(document.pop("id"))
        return document

    @staticmethod
    def _to_entity(document: dict) -> EmployeeDirectory:
        document = dict(document)
        document["id"] = document.pop("_id")
        return EmployeeDirectory(**document)