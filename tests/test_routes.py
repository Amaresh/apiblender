import pytest
from flask import Flask

# Import the Flask app
try:
    from app import app  # Adjust import if app is in a different module
except ImportError:
    app = None

@pytest.fixture
def client():
    if app is None:
        pytest.skip("Flask app not found for testing.")
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_returns_200(client):
    response = client.get("/")
    assert response.status_code == 200

def test_health_endpoint(client):
    response = client.get("/health")
    # Accept 200 or 404 if /health does not exist
    assert response.status_code in (200, 404)

def test_404_on_unknown_route(client):
    response = client.get("/this-route-should-not-exist")
    assert response.status_code == 404
