FROM python:3.7

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENTRYPOINT ["gunicorn", "--workers=3", "app:app"]

