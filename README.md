1. Clone the repo

```
git clone https://github.com/theparadoxer02/pratilipi.git
cd pratilipi
virtualenv -p python3 venv
source venv/bin/activate
```

2. Install requirements file

```
cd pvr
pip install -r  requirements.txt
```

3. Create Postgres Database name `pratilipidb`
Update Database setting in `pvr/settings.py` file

e.g Setup
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'pratilipidb',
        'USER': 'pratilipi_user',
        'PASSWORD': 'paratilipi_pass',
        'HOST': 'localhost',
        'PORT': '',
    }
}
```

4. Migrations
```
python manage.py makemigrations
python manage.py migrate
```
5. Run Server
```
python manage.py runserver
```

6. CREATE SUPERUSER
```
python manage.py createsuperuser
```

7. Go to url localhost:8000/admin and create some dump database like country, city, movie theatre etc.

8. Some URL endpoints are

    - Signup Form: `http://localhost:8000`
    - Send Mail Form: `http://localhost:8000/sendmail/`
    - Admin URL : `http://localhost:8000/admin`


9. Tech Stack Used:
    - Django
    - Celery for asynchronous tasks of sending mails
    - Postgres