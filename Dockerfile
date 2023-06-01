FROM python:3.9

WORKDIR .
COPY . .
COPY requirements.txt .
COPY db_service/src/endpoints.py .

CMD pip install -r requirements.txt
CMD uvicorn endpoints:app --host 0.0.0.0
