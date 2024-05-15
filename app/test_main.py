from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Hi! For test, you should send POST request to the `/predict` endpoint, with following parameters:","body":{"longitude":1.2,"latitude":1.2,"housing_median_age":1.2,"total_rooms":1.2,"total_bedrooms":1.2,"population":1.2,"households":1.2,"median_income":1.2,"median_house_value":1.2,"ocean_proximity":"test"}}


def test_read_predict_positive():
    response = client.post("/predict",
        json={"longitude":1.2,"latitude":1.2,"housing_median_age":1.2,"total_rooms":1.2,"total_bedrooms":1.2,"population":1.2,"households":1.2,"median_income":1.2,"median_house_value":1.2,"ocean_proximity":"test"}
    )
    json_data = response.json() 

    assert response.status_code == 200
    assert json_data == {"result": 28.56030539788831}
