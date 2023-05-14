#Dockerfile of servis handling database connection
FROM python:3.9

WORKDIR /db_service
COPY . .

RUN pip uninstall kafka
RUN pip install -r requirements.txt
#RUN pip install mysql-connector-python
