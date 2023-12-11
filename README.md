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
        "test_mode": <true/false>,
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

## Deployment
Step by step guide to deploy the project on a server.

### Setup server
1. Install necessary software on the server.
```bash
sudo apt-get update
sudo apt-get install python3-pip python3-dev libpq-dev nginx curl
```
2. Create a new user and setup a virtual environment.

3. Clone the project from github.
Ensure that the VServer has access to the repository.

Clone the project into the home/workspace directory of the user.
```bash
git clone https://github.com/Jluelsdo/AirtecWebservice.git
```
4. Install dependencies
```bash
cd AirtecWebservice
pip install -r requirements.txt
```

5. Set up config.json in workspace folder

6. Migrate database and collect static files
```bash
python manage.py migrate
python manage.py collectstatic
```

7. Configure Gunicorn
```bash
gunicorn --bind 0.0.0.0:8000 AirtecWebservice.wsgi:application
```

8. Configure Nginx
```bash
sudo rm /etc/nginx/sites-enabled/default
sudo touch /etc/nginx/sites-available/AirtecWebservice
sudo ln -s /etc/nginx/sites-available/AirtecWebservice /etc/nginx/sites-enabled/AirtecWebservice
```
9 Add avaiable sites
```bash
server {
    listen 80;
    server_name your_domain www.your_domain;

    location = /favicon.ico { access_log off; log_not_found off; }
    location /static/ {
        root /home/username/myproject;
    }

    location / {
        include proxy_params;
        proxy_pass http://unix:/home/username/myproject/myproject.sock;
    }
}
```
10. Restart nginx
```bash
sudo systemctl restart nginx
```

11. Allow Nginx to use open port 80
```bash
sudo ufw allow 'Nginx Full'
```