
from uuid import uuid4

import pytest
from fastapi.testclient import TestClient

from main import app
from dependencies import get_employee_directory_repository
from repositories.in_memory_employee_directory_repository import InMemoryEmployeeDirectoryRepository


@pytest.fixture
def client():
    repository = InMemoryEmployeeDirectoryRepository()

    app.dependency_overrides[get_employee_directory_repository] = lambda: repository

    yield TestClient(app)

    app.dependency_overrides.clear()


def test_create_employee_directory_returns_201_and_the_created_employee(client):
    response = client.post(
        "/employee_directories/",
        json={
            "name": "John Hacker",
            "department": "Engineering",
            "role": "Backend Developer"
        }
    )

    assert response.status_code == 201
    assert response.json()["name"] == "John Hacker"
    assert response.json()["department"] == "Engineering"
    assert response.json()["role"] == "Backend Developer"


def test_get_missing_employee_directory_returns_404(client):
    response = client.get(f"/employee_directories/{uuid4()}")

    assert response.status_code == 404


def test_full_crud_flow(client):
    create = client.post(
        "/employee_directories/",
        json={
            "name": "Emmanuel Dev",
            "department": "Software Development",
            "role": "Backend Developer"
        }
    )

    assert create.status_code == 201

    employee_id = create.json()["id"]

    get_response = client.get(f"/employee_directories/{employee_id}")

    assert get_response.status_code == 200
    assert get_response.json()["name"] == "Emmanuel Dev"

    patch_response = client.patch(
        f"/employee_directories/{employee_id}",
        json={"role": "Senior Backend Developer"}
    )

    assert patch_response.status_code == 200
    assert patch_response.json()["role"] == "Senior Backend Developer"

    delete_response = client.delete(
        f"/employee_directories/{employee_id}"
    )

    assert delete_response.status_code == 204

    get_deleted_response = client.get(
        f"/employee_directories/{employee_id}"
    )

    assert get_deleted_response.status_code == 404
