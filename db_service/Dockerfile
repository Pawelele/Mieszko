#Dockerfile of servis handling database connection
FROM python:3.9

WORKDIR /db_service
COPY . .

RUN pip install -r requirements.txt

CMD ["scrapy", "crawl", "myfancycrawler"]