def test_salary_calculation_for_india(client):
    payload = {
        "full_name": "Rahul Verma",
        "job_title": "Software Engineer",
        "country": "India",
        "salary": 50000
    }

    create_response = client.post("/employees", json=payload)
    employee_id = create_response.json()["id"]

    response = client.get(f"/employees/{employee_id}/salary")

    assert response.status_code == 200
    data = response.json()
    assert data["employee_id"] == employee_id
    assert data["country"] == "India"
    assert data["gross_salary"] == 50000
    assert data["deduction_type"] == "TDS"
    assert data["deduction_amount"] == 5000
    assert data["net_salary"] == 45000


def test_salary_calculation_for_united_states(client):
    payload = {
        "full_name": "John Smith",
        "job_title": "QA Engineer",
        "country": "United States",
        "salary": 100000
    }

    create_response = client.post("/employees", json=payload)
    employee_id = create_response.json()["id"]

    response = client.get(f"/employees/{employee_id}/salary")

    assert response.status_code == 200
    data = response.json()
    assert data["employee_id"] == employee_id
    assert data["country"] == "United States"
    assert data["gross_salary"] == 100000
    assert data["deduction_type"] == "TDS"
    assert data["deduction_amount"] == 12000
    assert data["net_salary"] == 88000


def test_salary_calculation_for_other_country(client):
    payload = {
        "full_name": "Ali Khan",
        "job_title": "Analyst",
        "country": "UAE",
        "salary": 70000
    }

    create_response = client.post("/employees", json=payload)
    employee_id = create_response.json()["id"]

    response = client.get(f"/employees/{employee_id}/salary")

    assert response.status_code == 200
    data = response.json()
    assert data["employee_id"] == employee_id
    assert data["country"] == "UAE"
    assert data["gross_salary"] == 70000
    assert data["deduction_type"] == "NO_DEDUCTION"
    assert data["deduction_amount"] == 0
    assert data["net_salary"] == 70000


def test_salary_calculation_employee_not_found(client):
    response = client.get("/employees/999/salary")

    assert response.status_code == 404
    assert response.json() == {"detail": "Employee not found"}