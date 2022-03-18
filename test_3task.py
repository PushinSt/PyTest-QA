# -- coding: utf-8 --

import pytest    
import subprocess

#3 task. Функционал управления приложением

#Начальный тест, чтобы однозначно остановить сервер
def test_stop():
    result = ((subprocess.run(['webcalculator.exe', 'stop'], stdout=subprocess.PIPE)).stdout.decode('cp1251')).strip()
    assert (result == 'Пытаемся остановить Веб-калькулятор\r\nВеб-калькулятор остановлен')

# Проверка запуска, перезапуска со значениями по умолчанию 
host_1 = '127.0.0.1'
port_1 = '17678'
data_1 = [
    ('start', 'Запуск Веб-калькулятора на ' + host_1 + ':' + port_1 + '\r\nВеб-калькулятор запущен на ' + host_1 + ':' + port_1),
    ('restart', 'Пытаемся остановить Веб-калькулятор\r\nВеб-калькулятор остановлен\r\nЗапуск Веб-калькулятора на ' + host_1 + ':' + port_1 + '\r\nВеб-калькулятор запущен на ' + host_1 + ':' + port_1),       
    ('stop', 'Пытаемся остановить Веб-калькулятор\r\nВеб-калькулятор остановлен'),
]
@pytest.mark.parametrize("comand, answer", data_1)
def test_start_default_values(comand, answer):
    result = ((subprocess.run(['webcalculator.exe', comand], stdout=subprocess.PIPE)).stdout.decode('cp1251')).strip()
    assert (result == answer)


# Проверка запуска с различными параметрами 
data_2 = [
    ('localhost', '5413'),   
    ('127.0.0.1', '17678'),
    ('localhost', '12345'),
]
@pytest.mark.parametrize("host, port", data_2)
def test_start_dif_values(host, port):
    result = ((subprocess.run(['webcalculator.exe', 'start', host, port], stdout=subprocess.PIPE)).stdout.decode('cp1251')).strip()
    subprocess.run(['webcalculator.exe', 'stop'], stdout=subprocess.DEVNULL) #остановить сервер для запуска след теста
    assert (result == ('Запуск Веб-калькулятора на ' + host + ':' + port + '\r\nВеб-калькулятор запущен на ' + host + ':' + port))

# Проверка перезапуска на пользовательских параметрах
host_3 = '127.0.0.1'
port_3 = '12345'
data_3 = [
    (['webcalculator.exe', 'start', host_3, port_3], 'Запуск Веб-калькулятора на ' + host_3 + ':' + port_3 + '\r\nВеб-калькулятор запущен на ' + host_3 + ':' + port_3),
    (['webcalculator.exe', 'restart'], 'Пытаемся остановить Веб-калькулятор\r\nВеб-калькулятор остановлен\r\nЗапуск Веб-калькулятора на ' + host_3 + ':' + port_3 + '\r\nВеб-калькулятор запущен на ' + host_3 + ':' + port_3),       
    (['webcalculator.exe', 'stop'], 'Пытаемся остановить Веб-калькулятор\r\nВеб-калькулятор остановлен'),
]
@pytest.mark.parametrize("comand, answer", data_3)
def test_restart_dif_values(comand, answer):

    result = ((subprocess.run(comand, stdout=subprocess.PIPE)).stdout.decode('cp1251')).strip()
    assert (result == answer)


# Проверка повторного запуска приложения
data_4 = [
    (['webcalculator.exe', 'start'], ['webcalculator.exe', 'start']),
    (['webcalculator.exe', 'start', 'localhost', '5413'], ['webcalculator.exe', 'start', 'localhost', '5414']),       
    (['webcalculator.exe', 'start', 'localhost', '5413'], ['webcalculator.exe', 'start', '127.0.0.1', '5414']),
    (['webcalculator.exe', 'start', 'localhost', '5413'], ['webcalculator.exe', 'start', '127.0.0.1', '5413']),
]
@pytest.mark.parametrize("comand1, comand2", data_4)
def test_double_start(comand1, comand2):
    subprocess.run(comand1, stdout=subprocess.DEVNULL)
    result = ((subprocess.run(comand2, stdout=subprocess.PIPE)).stdout.decode('cp1251')).strip()
    subprocess.run(['webcalculator.exe', 'stop'], stdout=subprocess.DEVNULL)
    assert (result == 'Сервер уже запущен')



# Проверка выполнения неизвестной команды
def test_unknown_command():
    result = ((subprocess.run(['webcalculator.exe', 'sta'], stderr=subprocess.PIPE)).stderr.decode('cp1251')).strip()
    assert ('error: argument command: invalid choice:' in result)



# Проверка запуска с некорректными параметрами 
data_5 = [
    (['webcalculator.exe', 'start', 'localhost', '-1'],  'error:'), 
    (['webcalculator.exe', 'start', 'localhost', ''],  'error:'),       
    (['webcalculator.exe', 'start', '-1', '5413'],  'error:'), 
    (['webcalculator.exe', 'start', '', '5413'],  'error:'), 
    (['webcalculator.exe', 'start', '127.0.0.-1', '5413'],  'error:'),
    (['webcalculator.exe', 'start', '-1', '-1'], 'error:'), 
    (['webcalculator.exe', 'start', '', ''], 'error:'),
    (['webcalculator.exe', 'start', '-1', ''], 'error:'),
    (['webcalculator.exe', 'start', '', '-1'], 'error:'),   
]
@pytest.mark.parametrize("comand, answer", data_5)
def test_wrong_values(comand, answer):

    result = subprocess.run(comand, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE) 
    error = result.stderr.decode('cp1251').strip()
    subprocess.run(['webcalculator.exe', 'stop'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    assert (answer in error)
