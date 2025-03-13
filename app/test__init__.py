import pytest
from app import getWeather

def test_get_weather(mocker):
    # Mock requests.get
    mock_get = mocker.patch("main.request.get")
    
    # Set return values
    mock_get.retun_value.status_code = 200
    mock_get.return_value.json.return_value = {"temperature" ; 55, "condition": "Sunny"}