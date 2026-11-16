
from typing import List
from uuid import UUID

from models.employee_directory import (EmployeeDirectory,EmployeeDirectoryCreate,EmployeeDirectoryUpdate)

from repositories.employee_directory_repository import EmployeeDirectoryRepository


class EmployeeDirectoryNotFoundError(Exception):
    pass


class EmployeeDirectoryService:

    def __init__(self, repository: EmployeeDirectoryRepository):
        self.repository = repository

    def create_employee_directory(
        self, payload: EmployeeDirectoryCreate) -> EmployeeDirectory:

        employee_directory = EmployeeDirectory(
            name=payload.name,
            department=payload.department,
            role=payload.role
        )

        return self.repository.add(employee_directory)

    def list_employee_directories(self) -> List[EmployeeDirectory]:
        return self.repository.list()

    def get_employee_directory(self, employee_id: UUID) -> EmployeeDirectory:

        employee = self.repository.get(employee_id)

        if employee is None:
            raise EmployeeDirectoryNotFoundError(f"EmployeeDirectory {employee_id} not found")

        return employee

    def update_employee_directory(self,employee_id: UUID,payload: EmployeeDirectoryUpdate) -> EmployeeDirectory:

        data = payload.model_dump(exclude_unset=True)

        employee = self.repository.update(employee_id, data)

        if employee is None:
            raise EmployeeDirectoryNotFoundError(f"EmployeeDirectory {employee_id} not found")

        return employee

    def delete_employee_directory(self, employee_id: UUID) -> None:

        deleted = self.repository.delete(employee_id)

        if not deleted:
            raise EmployeeDirectoryNotFoundError(f"EmployeeDirectory {employee_id} not found")
