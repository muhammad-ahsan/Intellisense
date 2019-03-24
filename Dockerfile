FROM python:3.6.5-stretch
MAINTAINER Muhammad Ahsan <muhammad.ahsan@gmail.com>
WORKDIR /usr/src/app
RUN apt-get update
RUN apt-get -y install supervisor
COPY uwsgi.ini .
COPY supervisor.conf /etc/supervisor/conf.d/
COPY Pipfile ./
COPY Pipfile.lock ./
RUN pip install pipenv
RUN pipenv install -e

COPY app.py ./
COPY logg.conf/ ./
COPY swagger ./swagger
COPY intellisense ./intellisense
EXPOSE 8080
CMD ["supervisord", "-n"]