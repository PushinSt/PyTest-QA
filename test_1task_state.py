# -- coding: utf-8 --
import requests
import json
import pytest

#1 task. GET - state

host="127.0.0.1"
port = 17678


request="http://"+ str(host) + ":" + str(port) + "/api/state"
def test_State_status_0():
    response = requests.get(request)
    assert response.status_code == 200


def test_State_ContentType_0():
    response = requests.get(request)
    assert response.headers['Content-Type'] == "application/json"

#???
def test_State_len_json_0():
    response = requests.get(request)
    response_body = response.json()
    assert len(response_body) == 2

def test_State_StatusCode_0():
    response = requests.get(request)
    response_body = response.json()
    assert list(iter(response_body))[0] == "statusCode"

def test_State_State_0():
    response = requests.get(request)
    response_body = response.json()
    assert list(iter(response_body))[1] == "state"

def test_State_StatusCode_equals_0():
    response = requests.get(request)
    response_body = response.json()
    assert response_body["statusCode"] == 0


def test_State_State_equals_0():
    response = requests.get(request)
    response_body = response.json()
    assert response_body["state"] == "OК" # О-англ К-рус (как в ТЗ)
    #assert response_body["state"] == "OK" # О-англ О-англ (По логике должно быть так)




