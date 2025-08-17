def test_availability_available(client):
    response = client.get(
        "/properties/availability",
        params={"property_id": 1, "start_date": "2025-08-20", "end_date": "2025-08-25", "guests_quantity": 2}
    )
    assert response.status_code == 200
    data = response.json()
    assert "available" in data
    assert data["available"] in [True, False]
