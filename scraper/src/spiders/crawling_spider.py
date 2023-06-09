"""Crawler module"""
import json
import re

from bs4 import BeautifulSoup, Tag
from requests import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from kafka import KafkaProducer
from time import sleep

import logging

# Configure the logging module
logging.basicConfig(level=logging.DEBUG)

# Create a logger instance
logger = logging.getLogger(__name__)



class CrawlingSpider(CrawlSpider):
    """Contains method to crawl web pages"""

    # MS TODO: Exceptions handler for offers not having all properties

    name = "myfancycrawler"
    allowed_domains = ["domiporta.pl"]
    start_urls = ["https://www.domiporta.pl/"]

    rules = (
        Rule(
            LinkExtractor(allow=r"mieszkanie/wynajme/*[a-z]*(\?PageNumber=[0-9]*)*$"),
            callback="parse_html",
            follow=True,
        ),
    )

    main_index = 1
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        sleep(10)
        logging.disable()
        self.producer = KafkaProducer(
            bootstrap_servers=['kafka:9092'],
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
#portainer
    def parse(self, response, **kwargs):
        pass

    def parse_html(self, response: Response):
        """
        Parses delivered response to get articles contains concrete data
        :param response: html page
                :return:
        """

        soup = BeautifulSoup(response.text, "html.parser")
        datas = soup.findAll("article")

        for data in datas:
            clean_data = self.clean_data(data)
            print(clean_data)
            try:
                self.send_message('db_topic', str(
               {
                    "price": clean_data[0],
                    "price_for_m": clean_data[3],
                    "area": clean_data[1],
                    "rooms_amount": clean_data[2],
                    "title": clean_data[4],
                    "offer": "for rent" if "wynajem" in clean_data[10] or "wynajem" in clean_data[4] else "for sale",
                    "short_description": clean_data[10],
                    "href": self.start_urls[0] + self._get_href(data)[1:],
                    "image": self._get_image(data).split()[0].replace("\"", ""),
                    "city": clean_data[6].split()[1]
                }))
                self.main_index += 1
            except IndexError as ex:
                with open("log.txt", "w", encoding="utf-8") as log_file:
                    log_file.write(str(clean_data) + "\n" + str(ex))
        
    #MS TODO: TBD passing results to DB service

    def send_message(self, topic, message):
        self.producer.send(topic, str(message))
        self.producer.flush()
    
    @staticmethod
    def clean_data(data: Tag) -> list[str]:
        """
        Splits and cleans data
        :param data: Part of the html site
        :return: list with concrete information extracted from the text from data
        """

        return [
            re.sub(r'\\u\w{4}', "", el.strip()
                .replace("ą", "a")
                .replace("ć", "c")
                .replace("ę", "e")
                .replace("ł", "l")
                .replace("ń", "n")
                .replace("ó", "o")
                .replace("ś", "s")
                .replace("ź", "z")
                .replace("ż", "z")
                .replace("Ą", "A")
                .replace("Ć", "C")
                .replace("Ę", "E")
                .replace("Ł", "L")
                .replace("Ń", "N")
                .replace("Ó", "O")
                .replace("Ś", "S")
                .replace("Ź", "Z")
                .replace("Ż", "Z") 
                .replace("\u00a0", " "))
                .replace(",", ";")
            for el in data.text.split("\n")
            if el.strip().replace("\xa0", " ") != ""
               and el not in ("WYRÓŻNIONE", "OBEJRZANE", "Więcej", "Skontaktuj się")
        ]

    @staticmethod
    def _get_href(data: Tag) -> str:
        """
        finds string contains HTML reference
        :param data: part of HTML
        :return: HTML reference
        """
        regex = r"href=\"(.*)\""
        matches = re.search(regex, str(data), re.MULTILINE)
        return matches.group(1)

    @staticmethod
    def _get_image(data: Tag) -> str:
        """
        finds string contains HTML reference to offer image
        :param data: part of HTML
        :return: HTML reference
        """
        regex = r"data\-src=\"(.*)\""
        matches = re.search(regex, str(data), re.MULTILINE)
        return matches.group(1)
