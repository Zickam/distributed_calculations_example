FROM python:3.12

WORKDIR /usr/src/app

ADD . .

CMD ["python", "-u", "unit.py"]