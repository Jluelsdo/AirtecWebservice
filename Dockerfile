FROM alpine:3.14
WORKDIR /django

RUN apk update && apk upgrade

RUN apk add python3-dev
RUN apk add py3-pip

RUN mkdir ./airtecWebservice
ADD airtecWebservice ./airtecWebservice 

RUN pip3 install --upgrade pip
COPY airtecWebservice/requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt
COPY . /tmp/


ENV PORT=8000
EXPOSE 8000

WORKDIR /django/airtecWebservice

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]