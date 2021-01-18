### Boot server

Active a python virtual environment:

```bash
cd server
virtualenv -p /usr/bin/python3 env
source env/bin/activate
```

Install requirements:

```bash
pip install -r requirements.txt
```

Initialize database:

```bash
python manage.py makemigrations users
python manage.py makemigrations services
python manage.py migrate
```

Run server with local:

```bash
python manage.py runserver --noreload
```

Open with Chrome or FireFox : **127.0.0.1:8000**