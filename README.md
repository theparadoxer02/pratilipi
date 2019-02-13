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