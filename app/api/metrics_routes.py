from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.employee import (
    CountrySalaryMetricsResponse,
    JobTitleSalaryMetricsResponse,
)
from app.services.metrics_service import (
    get_country_salary_metrics_service,
    get_job_title_salary_metrics_service,
)

router = APIRouter(tags=["Salary Metrics"])


@router.get("/metrics/salary/country/{country}", response_model=CountrySalaryMetricsResponse)
def get_salary_metrics_by_country(country: str, db: Session = Depends(get_db)):
    result = get_country_salary_metrics_service(db, country)

    if not result or result.minimum_salary is None:
        raise HTTPException(status_code=404, detail="No employees found for this country")

    return {
        "country": country,
        "minimum_salary": round(result.minimum_salary, 2),
        "maximum_salary": round(result.maximum_salary, 2),
        "average_salary": round(result.average_salary, 2),
    }


@router.get("/metrics/salary/job-title/{job_title}", response_model=JobTitleSalaryMetricsResponse)
def get_salary_metrics_by_job_title(job_title: str, db: Session = Depends(get_db)):
    result = get_job_title_salary_metrics_service(db, job_title)

    if not result or result.average_salary is None:
        raise HTTPException(status_code=404, detail="No employees found for this job title")

    return {
        "job_title": job_title,
        "average_salary": round(result.average_salary, 2),
    }