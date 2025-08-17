def test_create_property(client):
    payload = {
        "title": "Casa de Praia",
        "address_street": "Rua das Flores",
        "address_number": "123",
        "address_neighborhood": "Centro",
        "address_city": "Florianópolis",
        "address_state": "SC",
        "country": "Brasil",
        "rooms": 3,
        "capacity": 6,
        "price_per_night": 150.0
    }
    response = client.post("/properties/", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == payload["title"]
    assert data["capacity"] == 6

def test_get_property(client):
    response = client.get("/properties/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert data["title"] == "Casa de Praia"
