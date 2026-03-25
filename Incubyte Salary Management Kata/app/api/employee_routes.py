from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.employee import EmployeeCreate, EmployeeResponse
from app.services.employee_service import (
    create_employee_service,
    get_employee_service,
    list_employees_service,
)

router = APIRouter()


@router.post("/employees", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee(employee: EmployeeCreate, db: Session = Depends(get_db)):
    return create_employee_service(db, employee)


@router.get("/employees/{employee_id}", response_model=EmployeeResponse)
def get_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = get_employee_service(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return employee


@router.get("/employees", response_model=list[EmployeeResponse])
def get_all_employees(db: Session = Depends(get_db)):
    return list_employees_service(db)