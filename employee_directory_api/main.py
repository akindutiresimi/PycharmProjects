from fastapi import FastAPI
from controllers.employee_directory_controller import router as employee_directory_router

app = FastAPI(title="EmployeeDirectory API")


app.include_router(employee_directory_router)