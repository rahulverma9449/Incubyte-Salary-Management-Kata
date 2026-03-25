def test_create_employee(client):
    response = client.post("/employees/", json={"name": "Alice", "salary": 50000})

    assert response.status_code == 200
    assert response.json()["name"] == "Alice"
