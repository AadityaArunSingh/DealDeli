FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 5002

ENV FLASK_APP=app.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=5002"]
