from sqlalchemy import func
from sqlalchemy.orm import Session
from app.models.employee import Employee
from app.schemas.employee import EmployeeCreate, EmployeeUpdate


def create_employee(db: Session, employee_data: EmployeeCreate) -> Employee:
    employee = Employee(
        full_name=employee_data.full_name.strip(),
        job_title=employee_data.job_title.strip(),
        country=employee_data.country.strip(),
        salary=employee_data.salary,
    )
    db.add(employee)
    db.commit()
    db.refresh(employee)
    return employee


def get_employee_by_id(db: Session, employee_id: int):
    return db.query(Employee).filter(Employee.id == employee_id).first()


def list_employees(db: Session):
    return db.query(Employee).order_by(Employee.id.asc()).all()


def update_employee(db: Session, employee_id: int, employee_data: EmployeeUpdate):
    employee = get_employee_by_id(db, employee_id)
    if not employee:
        return None

    employee.full_name = employee_data.full_name.strip()
    employee.job_title = employee_data.job_title.strip()
    employee.country = employee_data.country.strip()
    employee.salary = employee_data.salary

    db.commit()
    db.refresh(employee)
    return employee


def delete_employee(db: Session, employee_id: int):
    employee = get_employee_by_id(db, employee_id)
    if not employee:
        return None

    db.delete(employee)
    db.commit()
    return employee


def get_country_salary_metrics(db: Session, country: str):
    result = (
        db.query(
            func.min(Employee.salary).label("minimum_salary"),
            func.max(Employee.salary).label("maximum_salary"),
            func.avg(Employee.salary).label("average_salary"),
        )
        .filter(func.lower(Employee.country) == country.lower())
        .first()
    )
    return result


def get_job_title_average_salary(db: Session, job_title: str):
    result = (
        db.query(func.avg(Employee.salary).label("average_salary"))
        .filter(func.lower(Employee.job_title) == job_title.lower())
        .first()
    )
    return result