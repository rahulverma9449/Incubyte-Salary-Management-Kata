from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse,
    DeleteResponse,
    SalaryCalculationResponse,
)
from app.services.employee_service import (
    create_employee_service,
    get_employee_service,
    list_employees_service,
    update_employee_service,
    delete_employee_service,
)
from app.services.salary_service import calculate_salary_details

router = APIRouter(tags=["Employees"])


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


@router.put("/employees/{employee_id}", response_model=EmployeeResponse)
def update_employee(employee_id: int, employee: EmployeeUpdate, db: Session = Depends(get_db)):
    updated_employee = update_employee_service(db, employee_id, employee)
    if not updated_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return updated_employee


@router.delete("/employees/{employee_id}", response_model=DeleteResponse)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    deleted_employee = delete_employee_service(db, employee_id)
    if not deleted_employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"message": "Employee deleted successfully"}


@router.get("/employees/{employee_id}/salary", response_model=SalaryCalculationResponse)
def get_salary_details(employee_id: int, db: Session = Depends(get_db)):
    employee = get_employee_service(db, employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")
    return calculate_salary_details(employee)