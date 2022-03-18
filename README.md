# Тестовое задание
на позицию «Автоматизированное тестирование (Python)»

### Задача:

>1)	Написать автоматические тесты (далее тесты), проверяющие корректность формата запроса/ответа для всех указанных в описании API-методов (раздел API интерфейс приложения)
>2)	Написать тесты, проверяющие основную функциональность приложения: правильность вычисления результата при указании допустимых входных данных. 
>3)	Проверить с помощью тестов функционал управления приложением (раздел Управление приложением): возможность смены адреса хоста/порта; значения по умолчанию; возможность остановки / перезапуска приложения.

### Дополнительное задание:
> 1) Реализовать несколько негативных тестов (например, проверяющие правильность возвращаемых кодов ошибок)
> 2) Предоставить автоматически сгенерированный отчет о результатах выполнения тестов основного задания в произвольном человеко-читаемом формате

### Требования к присылаемым решениям:
> 1)	Предоставить исходные файлы тестов 
> 2)	Тесты должны быть написаны на ЯП Python версии 3.x
> 3)	Ограничений на используемые встроенные и сторонние библиотеки нет

### Реализация
- Python 3.10.2.
- pip 21.2.4.
- pytest 7.0.1.
- pytest-html 3.1.1.
- pytest-metadata 1.11.0.
- requests 2.27.1.

Прежде, чем запустить процедуру тестирования сервера, необходимо его запустить в командной строке (cmd.exe, из каталога с решением):
```
webcalculator.exe start
```
Тесты запускаются из командной строки (cmd.exe, из каталога с решением) следующим образом: 
```
pytest --html=report\report.html --tb=no
```
После этого в командной строке можно наблюдать за ходом выполнения тестов. По итогу работы в каталоге report создается отчет о тестировании (report.html).


### Задание 1 (API интерфейс приложения):

Решение представлено пятью файлами (для каждой операции), в каждом файле реализованы следующие тесты:

Позитивные тесты:  
Проверка кода и заголовка возвращаемой страницы, проверка размера возвращаемой json структуры, проверка возвращаемой структуры json на соответствие формату из ТЗ.

Негативные тесты:  
Такие же проверки, только при некорректных условиях работы (ошибка вычисления, не хватает ключей в теле запроса, одно из значений не является целым числом, превышен размер одного из значений, неправильный формат тела запроса).

> Тесты запускаются на стандартных значениях хоста и порта (127.0.0.1 и 17678). В случае их изменения, необходимо внести изменения в исходный код тестов (8 и 9 строка текста).

### Задание 2 (правильность вычисления):

Решение представлено одним файлом, в котором реализованные тесты на различные числовые операции и проверка возможных ошибок вычисления (деление на ноль).

> Тесты запускаются на стандартных значениях хоста и порта (127.0.0.1 и 17678). В случае их изменения, необходимо внести изменения в исходный код тестов (8 и 9 строка текста).

### Задание 3 (функционал управления приложением):
Решение представлено одним файлом, в котором реализованные следующие тесты:

Позитивные:  
Проверка запуска/перезапуска сервера со значениями по умолчанию, проверка возможности смены адреса хоста/порта, проверка запуска/перезапуска сервера с пользовательскими значениями, остановка сервера.

Негативные:  
Проверка повторного запуска приложения, проверка выполнения неизвестной команды, проверка запуска с некорректными параметрами.



### Дополнительное задание (Негативные тесты и отчёт о тестировании):

Негативные тесты описаны в предыдущих пунктах.

Отчет о тестировании автоматически генерируется с помощью библиотеки pytest-html. В созданной html странице имеется информация об окружении, краткая информация о результатах тестирования и результат о каждом пройденном тесте (имя, результат, сообщение об ошибке, время выполнения).

Отчет(report.html) о тестировании находится в каталоге report.
