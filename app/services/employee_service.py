from sqlalchemy.orm import Session
from app.repositories.employee_repository import (
    create_employee,
    get_employee_by_id,
    list_employees,
    update_employee,
    delete_employee,
)
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


def create_employee_service(db: Session, employee_data: EmployeeCreate):
    return create_employee(db, employee_data)


def get_employee_service(db: Session, employee_id: int):
    return get_employee_by_id(db, employee_id)


def list_employees_service(db: Session):
    return list_employees(db)


def update_employee_service(db: Session, employee_id: int, employee_data: EmployeeUpdate):
    return update_employee(db, employee_id, employee_data)


def delete_employee_service(db: Session, employee_id: int):
    return delete_employee(db, employee_id)