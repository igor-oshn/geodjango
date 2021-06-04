GeoDjango

Изменить настройки БД в settings.py

Добавить свой API ключ для google map в шаблонах geo_django/locations/templates/[main.html, map_admin.html]

```javascript
<script src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY"></script>
```

```sh
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```
