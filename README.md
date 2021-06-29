Запуск:

Установить в файл .env переменную CONFIGURATION_TYPE=LOCAL

$pip install poetry. 

$poetry install. 

$source .venv/bin/activate. 
 
$docker-compose up -d. 

$bash events/run.sh. 


Тесты:
1. Заходим в сваггер: http://localhost:8001/docs (или пользуемся curl'ом)
2. Идем в Events, создаем экземпляры методом POST
Пример СURL для создания события:  
curl -X 'POST' \
  'http://localhost:8001/api/event/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Название события",
  "description": "Описание события",
  "city": "string",
  "start_time": "2021-06-28T21:12:15.847",
  "end_time": "2021-06-28T21:12:15.847"
}'
3. Создаем тему события:  
curl -X 'POST' \
  'http://localhost:8001/api/theme/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Тема"
}'
4. Создаем связь между событием и темой  
curl -X 'POST' \
  'http://localhost:8001/api/event-theme/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "event_id": <event_id>, # берем из нового event'а
  "theme_id": <theme_id> # берем из новой темы
}'
5. Чтобы отфильтровать события по городу выполняем следующий запрос:
curl -X 'GET' \
  'http://localhost:8001/api/events/?filters={"filters": [{"name": "city", "op": "eq", "val": "Москва"}]}&related_fields=true' \
  -H 'accept: application/json'

filters - формат фильтра
related_fields - для вывода инфы из соседних таблиц (без них есть баг)

6. Чтобы отфильтровать по диапазону дат:
curl -X 'GET' \
  'http://localhost:8001/api/events/?filters={"filters": [{"name": "start_time", "op": "between", "val": ["2021-06-27T19:26:30", "2021-06-27T19:26:31"]}]}&related_fields=true' \
  -H 'accept: application/json'

7. Чтобы отфильтровать по имени события:
curl -X 'GET' \
  'http://localhost:8001/api/events/?filters={"filters": [{"name": "theme.name", "op": "eq", "val": "Футбол"}]}&related_fields=true' \
  -H 'accept: application/json'

8. Чтобы сохранить фильтр:

8.1. Cоздадим юзера:
curl -X 'POST' \
  'http://localhost:8001/api/user/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "string",
  "email": "string",
  "password_hash": "string",
  "access_token": "string",
  "expires_at": "2021-06-28T21:36:26.082"
}'
8.2. Cоздаем сам фильтр:
curl -X 'POST' \
  'http://localhost:8001/api/filter' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Фильтр",
  "filter_body": "[{\"name\": \"city\", \"op\": \"eq\", \"val\": \"Москва\"}]", # тело фильтра
  "user_id": 1 # ид пользователя из предыдущего запроса
}'
