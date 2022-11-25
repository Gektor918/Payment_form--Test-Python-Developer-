
<h1>Тестовое задание для Python разработчика</h1>

<h2>Инструкция по запуску:</h2>

<h3>1. Клонируем репозиторий </h3>
&nbsp &nbsp &nbsp Команда - git clone https://github.com/Gektor918/Payment_form--Test-Python-Developer-

<h3>2. Создаем виртуальное окружение</h3>
&nbsp &nbsp &nbsp Команда - python3 -m venv name_venv

<h3>3. Запускаем виртуальное окружение</h3>
&nbsp &nbsp &nbsp Команда - source name_venv/bin/activate <br>

<h3>4. Устанавливаем зависимости</h3>
&nbsp &nbsp &nbsp Не забываем обновить pip Команда - pip install --upgrade pip
&nbsp &nbsp &nbsp Команда - pip install -r requirements.txt

<h3>5. Скачивание и установка PostgresSQL 14 </h3>
&nbsp &nbsp &nbsp Скачаиваем  PostgreSQL 14.6 Windows x86-64 <br>
&nbsp &nbsp &nbsp Ссылка для выбора версий https://www.enterprisedb.com/downloads/postgres-postgresql-downloads <br>
&nbsp &nbsp &nbsp Запустить скачанный файл и выполнить инструкцию по установке <br>
&nbsp &nbsp &nbsp Создайте локальную базу данных с такими параметрами: <br>
&nbsp &nbsp &nbsp 'NAME' : 'payment', <br>
&nbsp &nbsp &nbsp 'USER' : 'postgres', <br>
&nbsp &nbsp &nbsp 'PASSWORD' : '918',

<h3>6. Настройка Django</h3>
&nbsp &nbsp &nbsp Если вы работает в VS Code не забудте перейти от глобального интерпретатора к интерпретатору созданного окружения
&nbsp &nbsp &nbsp Вносим изменения &nbsp &nbsp python manage.py makemigrations main_app <br>
&nbsp &nbsp &nbsp Создаем таблицы в базе данных &nbsp &nbsp python manage.py migrate <br>
&nbsp &nbsp &nbsp Создайте пользователя с правами администратора &nbsp &nbsp python manage.py createsuperuser <br>
&nbsp &nbsp &nbsp Запустите сервер &nbsp &nbsp python manage.py runserver

<h3>7. Настройка панели Администратора</h3>
&nbsp &nbsp &nbsp В панели администратора найдите и добавте запись в Items: <br>
&nbsp &nbsp &nbsp Название товара == Xiaomi – Mi TV 4A 32 (Телевизор) <br>
&nbsp &nbsp &nbsp Описание == Наслаждайтесь контентом для всей семьи проще, быстрее и безопаснее <br>
&nbsp &nbsp &nbsp Цена == 80000 (Центов) <br>
&nbsp &nbsp &nbsp Нажмите сохранить <br>

<h3>8. Прочее</h3>
&nbsp &nbsp &nbsp http://127.0.0.1:8000/main_app/product - адрес страницы с продуктом <br>
&nbsp &nbsp &nbsp http://127.0.0.1:8000/main_app/cancel - адрес страницы с отменой <br>
&nbsp &nbsp &nbsp http://127.0.0.1:8000/main_app/success - адрес страницы с успешной оплатой <br>


