from main import app
from main import TestClient

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "version": "1.0"}

def test_unauthorized_access():
    response = client.get("/coins")
    assert response.status_code == 422

def test_invalid_authentication():
    response = client.get("/coins", params={"api_key": "wrong_key"})
    assert response.status_code == 401

def test_list_coins():
    response = client.get("/coins", params={"api_key": "123", "page_num": 1, "per_page": 5})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_list_categories():
    response = client.get("/categories", params={"api_key": "456", "page_num": 1, "per_page": 5})
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_coin():
    coin_id = "bitcoin"
    
    response = client.get(f"/coin/{coin_id}", params={"api_key": "123", "page_num": 1, "per_page": 5, "localization": "false"})

    assert response.status_code == 200

    data = response.json()
    assert "id" in data
    assert "name" in data
    assert "symbol" in data
    assert "current_price" in data

    assert data["current_price"] is not None
