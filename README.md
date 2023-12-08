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

### Configurations through config.json
To seperate the configuration from the code, a config.json file is used.
The file has to be included in the root directory of the project.
The json file has the following settings:
```{
        "secret_key": "<secret_key provided, ask jonas.luelsdorf@th-koeln.de >",
        "debug_mode": <true/false>,
        "allowed_hosts": "<allowed hosts, eg. on local localhost:8000 >",
        "static_root": "<location staticfiles e.g. ../../staticfiles >",
        "media_root": "<location mediafiles e.g. ../../mediafiles >"
    }
```
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