def test_create_reservation(client):
    payload = {
        "property_id": 1,
        "client_name": "João Silva",
        "client_email": "joaosilva@teste.com",
        "start_date": "2025-08-08",
        "end_date": "2025-08-09",
        "guests_quantity": 4
    }
    response = client.post("/reservations/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["property_id"] == 1
    assert data["guests_quantity"] == 4
