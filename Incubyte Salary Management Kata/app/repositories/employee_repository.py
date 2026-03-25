from sqlalchemy.orm import Session
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate


def create_employee(db: Session, employee_data: EmployeeCreate) -> Employee:
    employee = Employee(
        full_name=employee_data.full_name,
        job_title=employee_data.job_title,
        country=employee_data.country,
        salary=employee_data.salary
    )
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


def get_employee_by_id(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()


def list_employees(db: Session):
    return db.query(Employee).all()