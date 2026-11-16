
from uuid import uuid4

import pytest

from models.employee_directory import EmployeeDirectoryCreate, EmployeeDirectoryUpdate
from repositories.in_memory_employee_directory_repository import InMemoryEmployeeDirectoryRepository
from services.employee_directory_service import (
    EmployeeDirectoryService,
    EmployeeDirectoryNotFoundError
)


def test_create_employee_directory_returns_an_employee_with_the_given_name():
    service = EmployeeDirectoryService(InMemoryEmployeeDirectoryRepository())

    employee_directory = service.create_employee_directory(
        EmployeeDirectoryCreate(
            name="John Hacker",
            department="Engineering",
            role="Backend Developer"
        )
    )

    assert employee_directory.name == "John Hacker"
    assert employee_directory.department == "Engineering"
    assert employee_directory.role == "Backend Developer"


def test_get_employee_directory_raises_when_it_does_not_exist():
    service = EmployeeDirectoryService(InMemoryEmployeeDirectoryRepository())

    with pytest.raises(EmployeeDirectoryNotFoundError):
        service.get_employee_directory(uuid4())


def test_delete_employee_directory_removes_it_from_the_repository():
    service = EmployeeDirectoryService(InMemoryEmployeeDirectoryRepository())

    employee_directory = service.create_employee_directory(
        EmployeeDirectoryCreate(
            name="John Hacker",
            department="Engineering",
            role="Backend Developer"
        )
    )

    service.delete_employee_directory(employee_directory.id)

    with pytest.raises(EmployeeDirectoryNotFoundError):
        service.get_employee_directory(employee_directory.id)

def test_update_employee_directory_return_new_employee_directory_with_given_role():
    service = EmployeeDirectoryService(InMemoryEmployeeDirectoryRepository())

    employee_directory = service.create_employee_directory(
        EmployeeDirectoryCreate(
            name="John Hacker",
            department="Engineering",
            role="Backend Developer"
        )
    )
    assert employee_directory.name == "John Hacker"
    assert employee_directory.department == "Engineering"
    assert employee_directory.role == "Backend Developer"


    employee_directory = service.update_employee_directory(
        employee_directory.id,
        EmployeeDirectoryUpdate(
            name="john hacker",
            department="Engineering",
            role="fullstack developer"
        )
    )

    assert employee_directory.name == "john hacker"
    assert employee_directory.department == "Engineering"
    assert employee_directory.role == "fullstack developer"


def test_update_employee_directory_return_new_employee_directory_with_given_name_and_role():
    service = EmployeeDirectoryService(InMemoryEmployeeDirectoryRepository())

    employee_directory = service.create_employee_directory(
        EmployeeDirectoryCreate(
            name="John Hacker",
            department="Engineering",
            role="Backend Developer"
        )
    )
    assert employee_directory.name == "John Hacker"
    assert employee_directory.department == "Engineering"
    assert employee_directory.role == "Backend Developer"


    employee_directory = service.update_employee_directory(
        employee_directory.id,
        EmployeeDirectoryUpdate(
            name="emmanuel dev",
            department="Engineering",
            role="fullstack developer"
        )
    )

    assert employee_directory.name == "emmanuel dev"
    assert employee_directory.department == "Engineering"
    assert employee_directory.role == "fullstack developer"