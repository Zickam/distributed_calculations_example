FROM python:3.12

WORKDIR /usr/src/app

ADD unit_requirements.txt ./
RUN pip install --no-cache-dir --no-deps -r unit_requirements.txt

ADD . .

CMD ["python", "-u", "unit.py"]