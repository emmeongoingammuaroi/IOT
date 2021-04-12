# IOT smart home

First, clone the repository to your local machine:

```bash
git clone https://github.com/Nukukoricchio/IOT
```

## 1. Boot server

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
Before following the next step, please read notes at server/README.MD

Run server with local:

```bash
python manage.py runserver --noreload
```

Open with Chrome or FireFox : **127.0.0.1:8000**

# Notes

There are some notes you need to notice:

1. You have to change the '.env.example' filename to '.env'

2. You need to change all value in services/constants.py file with the right value of your broker


## 2. Boot Vue frontend

Install node packages:

```bash
cd frontend
npm install
```

Before following the next step, please read notes at frontend/README.MD

Run Vue with local:

```bash
npm run dev
```

Open with Chrome or FireFox : **localhost:8080**
