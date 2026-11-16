from fastapi import Depends

from repositories.employee_directory_repository import EmployeeDirectoryRepository
from repositories.in_memory_employee_directory_repository import InMemoryEmployeeDirectoryRepository
from services.employee_directory_service import EmployeeDirectoryService

_repository = InMemoryEmployeeDirectoryRepository()

def get_employee_directory_repository() -> EmployeeDirectoryRepository:
    return _repository

def get_employee_directory_service(repository: EmployeeDirectoryRepository = Depends(get_employee_directory_repository),) -> EmployeeDirectoryService:
    return EmployeeDirectoryService(repository)