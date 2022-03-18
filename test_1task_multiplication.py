# -- coding: utf-8 --
import requests
import json
import pytest

#1 task. POST - multiplication

host="127.0.0.1"
port = 17678


#multiplication - верные данные (0)
request_0="http://"+ str(host) + ":" + str(port) + "/api/multiplication"
data_0=json.dumps({'x': 1, 'y': 2})

def test_Mul_status_0():
    response = requests.post(request_0, data_0)
    assert response.status_code == 200

def test_Mul_ContentType_0():
    response = requests.post(request_0, data_0)
    assert response.headers['Content-Type'] == "application/json"

def test_Mul_len_json_0():
    response = requests.post(request_0, data_0)
    response_body = response.json()
    assert len(response_body) == 2

def test_Mul_StatusCode_0():
    response = requests.post(request_0, data_0)
    response_body = response.json()
    assert list(iter(response_body))[0] == "statusCode"

def test_Mul_Result_0():
    response = requests.post(request_0, data_0)
    response_body = response.json()
    assert list(iter(response_body))[1] == "result"

def test_Mul_StatusCode_equals_0():
    response = requests.post(request_0, data_0)
    response_body = response.json()
    assert response_body["statusCode"] == 0

def test_Mul_Result_equals_0():
    response = requests.post(request_0, data_0)
    response_body = response.json()
    assert response_body["result"] == 2 




#multiplication - ошибка вычисления (1) "Ошибка вычисления"
# для операции умножения нет таких тестов




#multiplication - не хватает ключей (2) "Не указаны необходимые параметры"
request_2="http://"+ str(host) + ":" + str(port) + "/api/multiplication"
data_2_x=json.dumps({'x': 1})

def test_Mul_status_2_x():
    response = requests.post(request_2, data_2_x)
    assert response.status_code == 200

def test_Mul_ContentType_2_x():
    response = requests.post(request_2, data_2_x)
    assert response.headers['Content-Type'] == "application/json"

def test_Mul_len_json_2_x():
    response = requests.post(request_2, data_2_x)
    response_body = response.json()
    assert len(response_body) == 2

def test_Mul_StatusCode_2_x():
    response = requests.post(request_2, data_2_x)
    response_body = response.json()
    assert list(iter(response_body))[0] == "statusCode"

def test_Mul_StatusMessage_2_x():
    response = requests.post(request_2, data_2_x)
    response_body = response.json()
    assert list(iter(response_body))[1] == "statusMessage"

def test_Mul_StatusCode_equals_2_x():
    response = requests.post(request_2, data_2_x)
    response_body = response.json()
    assert response_body["statusCode"] == 2

def test_Mul_StatusMessage_equals_2_x():
    response = requests.post(request_2, data_2_x)
    response_body = response.json()
    #assert response_body["statusMessage"] == "Не указаны необходимые параметры" # По факту выводит
    assert response_body["statusMessage"] == "Не хватает ключей в теле запроса" # По ТЗ


data_2_y=json.dumps({'y': 2})

def test_Mul_status_2_y():
    response = requests.post(request_2, data_2_y)
    assert response.status_code == 200

def test_Mul_ContentType_2_y():
    response = requests.post(request_2, data_2_y)
    assert response.headers['Content-Type'] == "application/json"

def test_Mul_len_json_2_y():
    response = requests.post(request_2, data_2_y)
    response_body = response.json()
    assert len(response_body) == 2

def test_Mul_StatusCode_2_y():
    response = requests.post(request_2, data_2_y)
    response_body = response.json()
    assert list(iter(response_body))[0] == "statusCode"

def test_Mul_StatusMessage_2_y():
    response = requests.post(request_2, data_2_y)
    response_body = response.json()
    assert list(iter(response_body))[1] == "statusMessage"

def test_Mul_StatusCode_equals_2_y():
    response = requests.post(request_2, data_2_y)
    response_body = response.json()
    assert response_body["statusCode"] == 2

def test_Mul_StatusMessage_equals_2_y():
    response = requests.post(request_2, data_2_y)
    response_body = response.json()
    #assert response_body["statusMessage"] == "Не указаны необходимые параметры" # По факту выводит
    assert response_body["statusMessage"] == "Не хватает ключей в теле запроса" # По ТЗ


data_2_=json.dumps({})

def test_Mul_status_2_():
    response = requests.post(request_2, data_2_)
    assert response.status_code == 200

def test_Mul_ContentType_2_():
    response = requests.post(request_2, data_2_)
    assert response.headers['Content-Type'] == "application/json"

def test_Mul_len_json_2_():
    response = requests.post(request_2, data_2_)
    response_body = response.json()
    assert len(response_body) == 2

def test_Mul_StatusCode_2_():
    response = requests.post(request_2, data_2_)
    response_body = response.json()
    assert list(iter(response_body))[0] == "statusCode"

def test_Mul_StatusMessage_2_():
    response = requests.post(request_2, data_2_)
    response_body = response.json()
    assert list(iter(response_body))[1] == "statusMessage"

def test_Mul_StatusCode_equals_2_():
    response = requests.post(request_2, data_2_)
    response_body = response.json()
    assert response_body["statusCode"] == 2

def test_Mul_StatusMessage_equals_2_():
    response = requests.post(request_2, data_2_)
    response_body = response.json()
    #assert response_body["statusMessage"] == "Не указаны необходимые параметры" # По факту выводит
    assert response_body["statusMessage"] == "Не хватает ключей в теле запроса" # По ТЗ





#multiplication - Одно из значений не является целым числом (3)
data_3 = [
    (1.5, 2),
    (1, 2.5),
    (1.5, 2.5), 
    ("", 2), 
    (1, ""),
    ("", ""),   
]

@pytest.mark.parametrize("x, y", data_3)
def test_Mul_status_3(x,y):
    response = requests.post(request_0, json.dumps({'x': x, 'y': y}))
    assert response.status_code == 200

@pytest.mark.parametrize("x, y", data_3)
def test_Mul_ContentType_3(x,y):
    response = requests.post(request_0, json.dumps({'x': x, 'y': y}))
    assert response.headers['Content-Type'] == "application/json"

@pytest.mark.parametrize("x, y", data_3)
def test_Mul_len_json_3(x,y):
    response = requests.post(request_0, json.dumps({'x': x, 'y': y}))
    response_body = response.json()
    assert len(response_body) == 2

@pytest.mark.parametrize("x, y", data_3)
def test_Mul_StatusCode_3(x,y):
    response = requests.post(request_0, json.dumps({'x': x, 'y': y}))
    response_body = response.json()
    assert list(iter(response_body))[0] == "statusCode"

@pytest.mark.parametrize("x, y", data_3)
def test_Mul_Result_3(x,y):
    response = requests.post(request_0, json.dumps({'x': x, 'y': y}))
    response_body = response.json()
    assert list(iter(response_body))[1] == "statusMessage"

@pytest.mark.parametrize("x, y", data_3)
def test_Mul_StatusCode_equals_3(x,y):
    response = requests.post(request_0, json.dumps({'x': x, 'y': y}))
    response_body = response.json()
    assert response_body["statusCode"] == 3

@pytest.mark.parametrize("x, y", data_3)
def test_Mul_Result_equals_3(x,y):
    response = requests.post(request_0, json.dumps({'x': x, 'y': y}))
    response_body = response.json()
    #assert response_body["statusMessage"] == "Значения параметров должны быть целыми" # по факту
    assert response_body["statusMessage"] == "Одно из значений не является целым числом" #из ТЗ




#multiplication - Превышен размер одного из значений (4)
data_4 = [
    (2147483648, 0), 
    (0, 2147483648), 
    (2147483649, 0),
    (0, 2147483649), 
    (-147483649, 0),
    (0, -2147483649), 
    (-147483650, 0),
    (0, -2147483650), 
]

@pytest.mark.parametrize("x, y", data_4)
def test_Mul_status_4(x,y):
    response = requests.post(request_0, json.dumps({'x': x, 'y': y}))
    assert response.status_code == 200

@pytest.mark.parametrize("x, y", data_4)
def test_Mul_ContentType_4(x,y):
    response = requests.post(request_0, json.dumps({'x': x, 'y': y}))
    assert response.headers['Content-Type'] == "application/json"

@pytest.mark.parametrize("x, y", data_4)
def test_Mul_len_json_4(x,y):
    response = requests.post(request_0, json.dumps({'x': x, 'y': y}))
    response_body = response.json()
    assert len(response_body) == 2

@pytest.mark.parametrize("x, y", data_4)
def test_Mul_StatusCode_4(x,y):
    response = requests.post(request_0, json.dumps({'x': x, 'y': y}))
    response_body = response.json()
    assert list(iter(response_body))[0] == "statusCode"

@pytest.mark.parametrize("x, y", data_4)
def test_Mul_Result_4(x,y):
    response = requests.post(request_0, json.dumps({'x': x, 'y': y}))
    response_body = response.json()
    assert list(iter(response_body))[1] == "statusMessage"

@pytest.mark.parametrize("x, y", data_4)
def test_Mul_StatusCode_equals_4(x,y):
    response = requests.post(request_0, json.dumps({'x': x, 'y': y}))
    response_body = response.json()
    assert response_body["statusCode"] == 4

@pytest.mark.parametrize("x, y", data_4)
def test_Mul_Result_equals_4(x,y):
    response = requests.post(request_0, json.dumps({'x': x, 'y': y}))
    response_body = response.json()
    #assert response_body["statusMessage"] == "Превышены максимальные значения параметров" # по факту
    assert response_body["statusMessage"] == "Превышен размер одного из значений" #из ТЗ





#multiplication -  Неправильный формат тела запроса (5)
request_5="http://"+ str(host) + ":" + str(port) + "/api/multi"
data_5=json.dumps({'x': 1, 'y': 2})

def test_Mul_status_5():
    response = requests.post(request_5, data_5)
    assert response.status_code == 200

def test_Mul_ContentType_5():
    response = requests.post(request_5, data_5)
    assert response.headers['Content-Type'] == "application/json"

def test_Mul_len_json_5():
    response = requests.post(request_5, data_5)
    response_body = response.json()
    assert len(response_body) == 2

def test_Mul_StatusCode_5():
    response = requests.post(request_5, data_5)
    response_body = response.json()
    assert list(iter(response_body))[0] == "statusCode"

def test_Mul_StatusMessage_5():
    response = requests.post(request_5, data_5)
    response_body = response.json()
    assert list(iter(response_body))[1] == "statusMessage"

def test_Mul_StatusCode_equals_5():
    response = requests.post(request_5, data_5)
    response_body = response.json()
    assert response_body["statusCode"] == 5

def test_Mul_StatusMessage_equals_5():
    response = requests.post(request_5, data_5)
    response_body = response.json()
    #assert response_body["statusMessage"] == " multi - Не верное имя задачи или тип HTTP запроса" # По факту выводит
    assert response_body["statusMessage"] == "Неправильный формат тела запроса" # По ТЗ