from fastapi.testclient import TestClient
import pytest
from fastapi.app import app

   
@pytest.fixture
def client():
    return TestClient(app)


def test_valid_predict(client):
    json=[{    
        "id":0,
        "gender":"H",
        "salary":1000.0,
        "company":"facebook",
        "position_level":1,
        "score": 3.0,
        "work_hours":20.10 ,
        "experience_years":23.0,
        "has_certifications":True,
        "promoted":True
        }]
    
    response = client.post("/predict", json=json)
    assert response.status_code == 200   
    
    
def test_invalid_predict(client):
    json=[{    
        "id":0,
        "promoted":True
        }]
    
    response = client.post("/predict", json=json)
    assert response.status_code == 400  
