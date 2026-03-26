from pydantic import BaseModel, Field


class EmployeeCreate(BaseModel):
    full_name: str = Field(..., min_length=1)
    job_title: str = Field(..., min_length=1)
    country: str = Field(..., min_length=1)
    salary: float = Field(..., gt=0)


class EmployeeUpdate(BaseModel):
    full_name: str = Field(..., min_length=1)
    job_title: str = Field(..., min_length=1)
    country: str = Field(..., min_length=1)
    salary: float = Field(..., gt=0)


class EmployeeResponse(BaseModel):
    id: int
    full_name: str
    job_title: str
    country: str
    salary: float

    model_config = {"from_attributes": True}


class DeleteResponse(BaseModel):
    message: str


class SalaryCalculationResponse(BaseModel):
    employee_id: int
    full_name: str
    country: str
    gross_salary: float
    deduction_type: str
    deduction_amount: float
    net_salary: float


class CountrySalaryMetricsResponse(BaseModel):
    country: str
    minimum_salary: float
    maximum_salary: float
    average_salary: float


class JobTitleSalaryMetricsResponse(BaseModel):
    job_title: str
    average_salary: float