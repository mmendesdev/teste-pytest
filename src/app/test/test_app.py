import pytest
from app import app  
from flask import jsonify

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_user(client):
    # Primeiro, cria um usuário para testar o GET
    response = client.post('/users', json={"name": "Alice", "email": "alice@example.com"})
    assert response.status_code == 201
    user_id = response.json['id']

    # Testa o GET para obter o usuário recém-criado
    response = client.get(f'/users/{user_id}')
    assert response.status_code == 200
    assert response.json == {"id": user_id, "name": "Alice", "email": "alice@example.com"}

def test_get_user_not_found(client):
    response = client.get('/users/999')
    assert response.status_code == 404
    assert response.json == {"error": "User not found"}

def test_create_user(client):
    response = client.post('/users', json={"name": "Bob", "email": "bob@example.com"})
    assert response.status_code == 201
    assert response.json['name'] == "Bob"
    assert response.json['email'] == "bob@example.com"

def test_update_user(client):
    response = client.post('/users', json={"name": "Brunna", "email": "Brunna@example.com"})
    assert response.status_code == 201
    user_id = response.json['id']

    response = client.put(f'/users/{user_id}', json={"name": "Matheus", "email": "matheus.mendes@example.com"})
    assert response.status_code == 200
    assert response.json['name'] == "Matheus Mendes"
    assert response.json['email'] == "matheus.mendes@example.com"

def test_update_user_not_found(client):

    response = client.put('/users/999', json={"name": "Jubiliu", "email": "jubileu@example.com"})
    assert response.status_code == 404
    assert response.json == {"error": "User not found"}
