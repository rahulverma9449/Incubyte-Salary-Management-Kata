def test_list_employees(client):
    client.post("/employees/", json={"name": "Carol", "salary": 70000})

    response = client.get("/employees/")

    assert response.status_code == 200
    assert len(response.json()) >= 1
