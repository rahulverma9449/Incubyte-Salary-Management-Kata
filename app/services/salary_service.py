def calculate_salary_details(employee):
    gross_salary = employee.salary
    country = employee.country.strip().lower()

    if country == "india":
        deduction_rate = 0.10
        deduction_type = "TDS"
    elif country in ("united states", "usa", "us"):
        deduction_rate = 0.12
        deduction_type = "TDS"
    else:
        deduction_rate = 0.0
        deduction_type = "NO_DEDUCTION"

    deduction_amount = round(gross_salary * deduction_rate, 2)
    net_salary = round(gross_salary - deduction_amount, 2)

    return {
        "employee_id": employee.id,
        "full_name": employee.full_name,
        "country": employee.country,
        "gross_salary": gross_salary,
        "deduction_type": deduction_type,
        "deduction_amount": deduction_amount,
        "net_salary": net_salary,
    }