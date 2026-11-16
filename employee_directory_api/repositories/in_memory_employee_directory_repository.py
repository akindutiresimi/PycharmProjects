from datetime import timezone, datetime
from typing import List, Optional
from uuid import UUID

from models.employee_directory import EmployeeDirectory
from repositories.employee_directory_repository import EmployeeDirectoryRepository


class InMemoryEmployeeDirectoryRepository(EmployeeDirectoryRepository):


    def __init__(self):
        self._employees_directories: List[EmployeeDirectory] = []

    def add(self,employee_directory: EmployeeDirectory) -> EmployeeDirectory:

        self._employees_directories.append(employee_directory)

        return employee_directory

    def get(self,employee_id: UUID) -> Optional[EmployeeDirectory]:

        for employee in self._employees_directories:

            if employee.id == employee_id:
                return employee

        return None

    def list(self) -> List[EmployeeDirectory]:

        return self._employees_directories

    def update(self,employee_id: UUID,data: dict) -> Optional[EmployeeDirectory]:

        employee = self.get(employee_id)

        if employee is None:
            return None

        updated = employee.model_copy(update={**data,"updated_at": datetime.now(timezone.utc)})

        index = self._employees_directories.index(employee)

        self._employees_directories[index] = updated

        return updated

    def delete(self, employee_id: UUID) -> bool:

        employee = self.get(employee_id)

        if employee is None:
            return False

        self._employees_directories.remove(employee)

        return True
