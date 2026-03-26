def test_update_employee_success(client):
    create_payload = {
        "full_name": "Rahul Verma",
        "job_title": "Software Engineer",
        "country": "India",
        "salary": 50000
    }

    create_response = client.post("/employees", json=create_payload)
    employee_id = create_response.json()["id"]

    update_payload = {
        "full_name": "Rahul Verma Updated",
        "job_title": "Senior Software Engineer",
        "country": "India",
        "salary": 80000
    }

    response = client.put(f"/employees/{employee_id}", json=update_payload)

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == employee_id
    assert data["full_name"] == "Rahul Verma Updated"
    assert data["job_title"] == "Senior Software Engineer"
    assert data["country"] == "India"
    assert data["salary"] == 80000


def test_update_employee_not_found(client):
    update_payload = {
        "full_name": "Rahul Verma Updated",
        "job_title": "Senior Software Engineer",
        "country": "India",
        "salary": 80000
    }

    response = client.put("/employees/999", json=update_payload)

    assert response.status_code == 404
    assert response.json() == {"detail": "Employee not found"}


def test_update_employee_invalid_salary(client):
    create_payload = {
        "full_name": "Rahul Verma",
        "job_title": "Software Engineer",
        "country": "India",
        "salary": 50000
    }

    create_response = client.post("/employees", json=create_payload)
    employee_id = create_response.json()["id"]

    update_payload = {
        "full_name": "Rahul Verma Updated",
        "job_title": "Senior Software Engineer",
        "country": "India",
        "salary": 0
    }

    response = client.put(f"/employees/{employee_id}", json=update_payload)

    assert response.status_code == 422