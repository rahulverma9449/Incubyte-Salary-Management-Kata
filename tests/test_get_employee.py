def test_get_employee_by_id_success(client):
    payload = {
        "full_name": "Rahul Verma",
        "job_title": "Backend Developer",
        "country": "India",
        "salary": 60000
    }

    create_response = client.post("/employees", json=payload)
    employee_id = create_response.json()["id"]

    response = client.get(f"/employees/{employee_id}")

    assert response.status_code == 200
    data = response.json()
    assert data["id"] == employee_id
    assert data["full_name"] == "Rahul Verma"
    assert data["job_title"] == "Backend Developer"
    assert data["country"] == "India"
    assert data["salary"] == 60000


def test_get_employee_by_id_not_found(client):
    response = client.get("/employees/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Employee not found"}