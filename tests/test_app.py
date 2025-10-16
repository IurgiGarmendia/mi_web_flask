import os
import sys
import pytest

# Ensure project root is on sys.path so `from app import app` works when pytest runs
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    res = client.get('/')
    assert res.status_code == 200
    assert b"Hola" in res.data or b"Flask" in res.data

def test_ping(client):
    res = client.get('/ping')
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}
