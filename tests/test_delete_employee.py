def test_delete_employee_success(client):
    payload = {
        "full_name": "Rahul Verma",
        "job_title": "Software Engineer",
        "country": "India",
        "salary": 50000
    }

    create_response = client.post("/employees", json=payload)
    employee_id = create_response.json()["id"]

    response = client.delete(f"/employees/{employee_id}")

    assert response.status_code == 200
    assert response.json() == {"message": "Employee deleted successfully"}

    get_response = client.get(f"/employees/{employee_id}")
    assert get_response.status_code == 404


def test_delete_employee_not_found(client):
    response = client.delete("/employees/999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Employee not found"}