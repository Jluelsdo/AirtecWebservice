# AirtecWebservice

## Virtual environment
Installation of virtual environment may differ from Linux/Windows
Highly recommended for tool and package management
### Create virtual environment

```bash
python3 -m venv venv
```

### install requirements
```bash
pip install -r requirements.txt
```
### add requirements
```bash
pip freeze > requirements.txt
```
Ensure that only requirements are added that are needed for the project.

## Start project

### Start server
```bash
python manage.py runserver
```

### Migrate database
```bash
python manage.py migrate
```

### Create superuser
```bash
python manage.py createsuperuser
```

### Collect static
```bash
python manage.py collectstatic
```
Must be executed after every change in static files, and when cloning the project.