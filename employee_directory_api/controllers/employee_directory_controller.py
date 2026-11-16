from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status

from dependencies import get_employee_directory_service
from models.employee_directory import EmployeeDirectory, EmployeeDirectoryCreate, EmployeeDirectoryUpdate
from services.employee_directory_service import EmployeeDirectoryService, EmployeeDirectoryNotFoundError

router = APIRouter(prefix="/employee_directories", tags=["EmployeeDirectory"])

@router.post("/", response_model=EmployeeDirectory, status_code=status.HTTP_201_CREATED)
def create_employee_directory(
    payload: EmployeeDirectoryCreate,
    service: EmployeeDirectoryService = Depends(get_employee_directory_service),
):
    return service.create_employee_directory(payload)

@router.get("/", response_model=list[EmployeeDirectory])
def list_employee_directories(service: EmployeeDirectoryService = Depends(get_employee_directory_service),
):
    return service.list_employee_directories()




@router.get("/{employee_id}", response_model=EmployeeDirectory)
def get_employee_directory(employee_id: UUID,service: EmployeeDirectoryService = Depends(get_employee_directory_service),
):
    try:
        return service.get_employee_directory(employee_id)
    except EmployeeDirectoryNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))



@router.patch("/{employee_id}", response_model=EmployeeDirectory)
def update_employee_directory(employee_id: UUID,payload: EmployeeDirectoryUpdate,service: EmployeeDirectoryService = Depends(get_employee_directory_service),
):
    try:
        return service.update_employee_directory(employee_id, payload)
    except EmployeeDirectoryNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))




@router.delete("/{employee_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_employee_directory(employee_id: UUID, service: EmployeeDirectoryService = Depends(get_employee_directory_service),
):
    try:
        service.delete_employee_directory(employee_id)
    except EmployeeDirectoryNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))