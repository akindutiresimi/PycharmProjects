from datetime import timezone, datetime
from typing import Optional
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class EmployeeDirectoryCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    department: str = Field(..., min_length=1, max_length=200)
    role: str = Field(..., min_length=1, max_length=200)


class EmployeeDirectoryUpdate(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    department: str = Field(..., min_length=1, max_length=200)
    role: str = Field(..., min_length=1, max_length=200)

class EmployeeDirectory(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str = Field(..., min_length=1, max_length=200)
    department: str = Field(..., min_length=1, max_length=200)
    role: str = Field(..., min_length=1, max_length=200)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))