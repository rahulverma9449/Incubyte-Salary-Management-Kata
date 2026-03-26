from app.repositories.employee_repository import (
    get_country_salary_metrics,
    get_job_title_average_salary,
)


def get_country_salary_metrics_service(db, country: str):
    return get_country_salary_metrics(db, country)


def get_job_title_salary_metrics_service(db, job_title: str):
    return get_job_title_average_salary(db, job_title)