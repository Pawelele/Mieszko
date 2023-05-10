"""Crawler module"""
import json
import re

from bs4 import BeautifulSoup, Tag
from requests import Response
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


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
        page_content = {}
        for data in datas:
            clean_data = self.clean_data(data)

            try:
                yield{
                    "price": clean_data[0],
                    "price_for_m": clean_data[3],
                    "area": clean_data[1],
                    "rooms_amount": clean_data[2],
                    "title": clean_data[4],
                    "offer": "for rent" if "wynajem" in clean_data[10] or "wynajem" in clean_data[4] else "for sale",
                    "short_description": clean_data[10],
                    "href": self.start_urls[0] + self._get_href(data)[1:],
                    "image": self._get_image(data),
                }
                self.main_index += 1
            except IndexError as ex:
                with open("log.txt", "w", encoding="utf-8") as log_file:
                    log_file.write(str(clean_data) + "\n" + str(ex))

        with open("offers.json", "w") as output:
            json.dump(page_content, output)
    #MS TODO: TBD passing results to DB service

    @staticmethod
    def clean_data(data: Tag) -> list[str]:
        """
        Splits and cleans data
        :param data: Part of the html site
        :return: list with concrete information extracted from the text from data
        """
        return [
            el.strip()
                .replace("\xa0", " ")
                .replace("\u0142", "ł")
                .replace("\u0105", "ą")
                .replace("\u0119", "ę")
                .replace("\u0118", "Ę")
                .replace("\u0144", "ń")
                .replace("\u0143", "Ń")
                .replace("\u015b", "ś")
                .replace("\u015a", "Ś")
                .replace("\u0107", "ć")
                .replace("\u017c", "ż")
                .replace("\u00d3", "ó")
                .replace("\u0141", "Ł")
                .replace("\u0104", "Ą")
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
