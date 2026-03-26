from fastapi import Request, status
from fastapi.responses import JSONResponse


class EmployeeNotFoundException(Exception):
    def __init__(self, employee_id: int):
        self.employee_id = employee_id
        self.message = f"Employee with id {employee_id} not found"
        super().__init__(self.message)


class CountryNotFoundException(Exception):
    def __init__(self, country: str):
        self.country = country
        self.message = f"No employees found for country '{country}'"
        super().__init__(self.message)


class JobTitleNotFoundException(Exception):
    def __init__(self, job_title: str):
        self.job_title = job_title
        self.message = f"No employees found for job title '{job_title}'"
        super().__init__(self.message)


async def employee_not_found_exception_handler(
    request: Request,
    exc: EmployeeNotFoundException
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": "Employee Not Found",
            "message": exc.message
        }
    )


async def country_not_found_exception_handler(
    request: Request,
    exc: CountryNotFoundException
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": "Country Data Not Found",
            "message": exc.message
        }
    )


async def job_title_not_found_exception_handler(
    request: Request,
    exc: JobTitleNotFoundException
):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={
            "error": "Job Title Data Not Found",
            "message": exc.message
        }
    )