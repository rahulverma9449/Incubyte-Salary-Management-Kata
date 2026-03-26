from fastapi import FastAPI
from app.database import Base, engine
from app.api.employee_routes import router as employee_router
from app.api.metrics_routes import router as metrics_router
from app.core.exceptions import (
    EmployeeNotFoundException,
    CountryNotFoundException,
    JobTitleNotFoundException,
    employee_not_found_exception_handler,
    country_not_found_exception_handler,
    job_title_not_found_exception_handler,
)

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Incubyte Salary Management API")

app.include_router(employee_router)
app.include_router(metrics_router)

app.add_exception_handler(
    EmployeeNotFoundException,
    employee_not_found_exception_handler
)
app.add_exception_handler(
    CountryNotFoundException,
    country_not_found_exception_handler
)
app.add_exception_handler(
    JobTitleNotFoundException,
    job_title_not_found_exception_handler
)