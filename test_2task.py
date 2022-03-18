# -- coding: utf-8 --
import requests
import json
import pytest

#2 task.

host="127.0.0.1"
port = 17678


#addition
request_0="http://"+ str(host) + ":" + str(port) + "/api/addition"
data_0 = [
    (0, 0, 0),
    (3, 5, 8),
    (-5, -3, -8), 
    (1073741823, 1073741824, 2147483647), 
    (-1073741824, -1073741824, -2147483648),
    (2147483647, 2147483647, 4294967294),   
    (-2147483648, -2147483648, -4294967296),  
]
@pytest.mark.parametrize("x, y, z", data_0)
def test_Add_equals(x,y,z):
    response = requests.post(request_0, json.dumps({'x': x, 'y': y}))
    response_body = response.json()
    assert response_body["result"] == z 



#multiplication
request_1="http://"+ str(host) + ":" + str(port) + "/api/multiplication"
data_1 = [
    (0, 0, 0),
    (0, 10, 0),
    (-10, 0, 0),
    (3, 5, 15),
    (-5, -3, 15), 
    (3, -5, -15),
    (5, -3, -15),
    (20853, 102982, 2147483646), 
    (-65536, 32768, -2147483648),
    (2147483647, 10, 21474836470),   
    (-2147483648, 10, -21474836480),  
]

@pytest.mark.parametrize("x, y, z", data_1)
def test_Mul_equals(x,y,z):
    response = requests.post(request_1, json.dumps({'x': x, 'y': y}))
    response_body = response.json()
    assert response_body["result"] == z 



#division
request_2="http://"+ str(host) + ":" + str(port) + "/api/division"
data_2 = [
    (0, 10, 0),
    (0, -10, 0),
    (9, 3, 3), 
    (9, -3, -3),
    (24, 4, 6),
    (23, 4, 5),
    (22, 4, 5),
    (21, 4, 5),
    (20, 4, 5),
    (-24, 4, -6),
    (-23, 4, -5),
    (-22, 4, -5),
    (-21, 4, -5),
    (-20, 4, -5), 
    (2147483647, 1, 2147483647),
    (2147483647, 100, 21474836),   
    (-2147483648, 1, -2147483648),  
    (-2147483648, 100, -21474836),
]

@pytest.mark.parametrize("x, y, z", data_2)
def test_Div_equals(x,y,z):
    response = requests.post(request_2, json.dumps({'x': x, 'y': y}))
    response_body = response.json()
    assert response_body["result"] == z 



#remainder
request_3="http://"+ str(host) + ":" + str(port) + "/api/remainder"
data_3 = [
    (0, 10, 0),
    (0, -10, 0),
    (9, 3, 0), 
    (9, -3, 0),
    (24, 4, 0),
    (23, 4, 3),
    (22, 4, 2),
    (21, 4, 1),
    (20, 4, 0),
    (-24, 4, 0),
    (-23, 4, 1),
    (-22, 4, 2),
    (-21, 4, 3),
    (-20, 4, 0), 
    (-23, -4, 1),
    (2147483647, 1, 0),
    (2147483647, 100, 47),   
    (-2147483648, 1, 0),  
    (-2147483648, 100, 52),
]

@pytest.mark.parametrize("x, y, z", data_3)
def test_Rem_equals(x,y,z):
    response = requests.post(request_3, json.dumps({'x': x, 'y': y}))
    response_body = response.json()
    assert response_body["result"] == z

