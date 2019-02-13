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

3. Update Database setting in `pvr/settings.py` file

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

    Signup Form: `http://localhost:8000`
    Send Mail Form: `http://localhost:8000/sendmail/`


9. Tech Stack Used:
    - Django
    - Celery for asynchronous tasks of sending mails
    - Postgres