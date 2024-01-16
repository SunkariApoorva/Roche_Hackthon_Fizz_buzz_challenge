import pytest
import requests
from fizzbuzz_server import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_fizz_buzz_endpoint(client):
    response = client.get('/fizzbuzz?int1=3&int2=5&limit=15&str1=fizz&str2=buzz')
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert data == ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']

def test_statistics_endpoint(client):
    # Make some requests to increment the counter
    client.get('/fizzbuzz?int1=3&int2=5&limit=10&str1=fizz&str2=buzz')
    client.get('/fizzbuzz?int1=2&int2=4&limit=8&str1=fizz&str2=buzz')
    client.get('/fizzbuzz?int1=3&int2=5&limit=10&str1=fizz&str2=buzz')

    response = client.get('/statistics')
    data = response.get_json()

    assert response.status_code == 200
    assert 'parameters' in data
    assert 'hits' in data
    assert data['parameters'] == {'int1': 3, 'int2': 5, 'limit': 10, 'str1': 'fizz', 'str2': 'buzz'}
    assert data['hits'] == 2

def test_invalid_fizz_buzz_parameters(client):
    response = client.get('/fizzbuzz?int1=3&int2=5&limit=15')
    data = response.get_json()

    assert response.status_code == 200
    assert isinstance(data, list)
    assert data == ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11', 'fizz', '13', '14', 'fizzbuzz']

def test_invalid_statistics_parameters(client):
    response = client.get('/statistics?invalid_param=123')
    data = response.get_json()

    assert response.status_code == 200
    assert 'hits' in data
    assert 'parameters' in data
    assert 'message' not in data  # Ensure 'message' key is not present

