FROM python:3.9

WORKDIR /app

COPY requirements.txt .
COPY . .

RUN pip install -r requirements.txt

# CMD uvicorn --host=0.0.0.0 --port 8000 main:app
CMD ["uvicorn", "--host=0.0.0.0", "--port", "8000", "main:app"]