FROM python:3.8
MAINTAINER Muhammad Ahsan <muhammad.ahsan@gmail.com>

RUN apt-get -q update && apt-get -y install supervisor && rm -rf /var/lib/apt/lists/*
WORKDIR /usr/src/app
COPY uwsgi.ini .
COPY supervisord.conf /etc/supervisor/conf.d/

COPY Pipfile ./
COPY Pipfile.lock ./

RUN pip install pipenv uwsgi

RUN pipenv lock --keep-outdated --requirements > requirements.txt
RUN pip install -r requirements.txt

COPY app.py ./
COPY swagger ./swagger
COPY intellisense ./intellisense

RUN ls

EXPOSE 5000

# Non production deployment
# CMD ["python", "app.py"]

# Production deployment
CMD ["supervisord", "-n"]
