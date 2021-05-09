# TODO(everyone): 웹서버의 healthz가 response code 200 확인
import requests
import pytest

def test():
    response = requests.get(url="http://localhost:800" + "/healthz")
    assert response.status_code == 200
