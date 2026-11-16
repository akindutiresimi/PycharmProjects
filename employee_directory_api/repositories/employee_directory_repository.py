
from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID

from models.employee_directory import EmployeeDirectory


class EmployeeDirectoryRepository(ABC):

    @abstractmethod
    def add(self, employee_directory: EmployeeDirectory) -> EmployeeDirectory:
        ...

    @abstractmethod
    def get(self, employee_id: UUID) -> Optional[EmployeeDirectory]:
        ...

    @abstractmethod
    def list(self) -> List[EmployeeDirectory]:
        ...

    @abstractmethod
    def update(
        self, employee_id: UUID, data: dict) -> Optional[EmployeeDirectory]:
        ...

    @abstractmethod
    def delete(self, employee_id: UUID) -> bool:
        ...

