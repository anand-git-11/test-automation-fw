import requests
from urllib.parse import urljoin
base_url = "https://api.example.com/v1/"


full_url = urljoin(base_url, path)

def test_api_1(input_param, server_connection):
    path = "users/123"
    res = requests.get(urljoin(base_url, path))
    assert res.ok, "Request failed"
    assert res.json() == input_param.exp_api_data, "Data mismatch"

def test_api_2(input_param, server_connection):
    path = "apps"
    res = requests.get(urljoin(base_url, path))
    assert res.ok, "Request failed"
    assert res.json() == input_param.exp_api_data, "Data mismatch"