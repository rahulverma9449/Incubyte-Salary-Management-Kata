from sqlalchemy.orm import Session
from app.repositories.employee_repository import (
    create_employee,
    get_employee_by_id,
    list_employees
)
from app.schemas.employee import EmployeeCreate


def create_employee_service(db: Session, employee_data: EmployeeCreate):
    return create_employee(db, employee_data)


def get_employee_service(db: Session, employee_id: int):
    return get_employee_by_id(db, employee_id)


def list_employees_service(db: Session):
    return list_employees(db)