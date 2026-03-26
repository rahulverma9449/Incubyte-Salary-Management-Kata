def test_salary_metrics_by_country_success(client):
    employees = [
        {
            "full_name": "Rahul Verma",
            "job_title": "Software Engineer",
            "country": "India",
            "salary": 50000
        },
        {
            "full_name": "Aman Kumar",
            "job_title": "Backend Engineer",
            "country": "India",
            "salary": 70000
        },
        {
            "full_name": "Priya Singh",
            "job_title": "QA Engineer",
            "country": "India",
            "salary": 90000
        }
    ]

    for employee in employees:
        client.post("/employees", json=employee)

    response = client.get("/metrics/salary/country/India")

    assert response.status_code == 200
    data = response.json()
    assert data["country"] == "India"
    assert data["minimum_salary"] == 50000
    assert data["maximum_salary"] == 90000
    assert data["average_salary"] == 70000


def test_salary_metrics_by_country_not_found(client):
    response = client.get("/metrics/salary/country/Canada")

    assert response.status_code == 404
    assert response.json() == {"detail": "No employees found for this country"}


def test_salary_metrics_by_job_title_success(client):
    employees = [
        {
            "full_name": "Rahul Verma",
            "job_title": "Software Engineer",
            "country": "India",
            "salary": 50000
        },
        {
            "full_name": "John Doe",
            "job_title": "Software Engineer",
            "country": "United States",
            "salary": 70000
        }
    ]

    for employee in employees:
        client.post("/employees", json=employee)

    response = client.get("/metrics/salary/job-title/Software Engineer")

    assert response.status_code == 200
    data = response.json()
    assert data["job_title"] == "Software Engineer"
    assert data["average_salary"] == 60000


def test_salary_metrics_by_job_title_not_found(client):
    response = client.get("/metrics/salary/job-title/Data Scientist")

    assert response.status_code == 404
    assert response.json() == {"detail": "No employees found for this job title"}