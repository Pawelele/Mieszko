from bs4 import BeautifulSoup
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CrawlingSpider(CrawlSpider):
	name = "myfancycrawler"
	allowed_domains = ["domiporta.pl"]
	start_urls = ["https://www.domiporta.pl/"]

	rules = (
		Rule(LinkExtractor(allow=(r"mieszkanie/wynajme/*[a-z]*(\?PageNumber=[0-9]*)*$")), callback="parse_html", follow=True),
	)

	def parse_html(self, response):
		soup = BeautifulSoup(response.text, "html.parser")
		datas = soup.findAll("article")
		for data in datas:
			clean_data = self.clean_data(data)
			yield {
				"price": clean_data[0],
				"price_for_m": clean_data[3],
				"area": clean_data[1],
				"rooms_amount": clean_data[2],
				"title": clean_data[4],
				"offer": "for rent" if "wynajem" in clean_data[10] or "wynajem" in clean_data[4] else "for sale",
				"short_description": clean_data[10],
			}

	def clean_data(self, data):
		return [el.strip().replace("\xa0", " ") for el in data.text.split("\n") if
				el.strip().replace("\xa0", " ") != "" and el not in (
				'WYRÓŻNIONE', 'OBEJRZANE', 'Więcej', 'Skontaktuj się')]
