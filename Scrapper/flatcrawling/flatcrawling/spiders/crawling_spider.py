from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CrawlingSpider(CrawlSpider):
	name = "myfancycrawler"
	allowed_domains = ["domiporta.pl"]
	start_urls = ["https://www.domiporta.pl/"]

	rules = (
		Rule(LinkExtractor(allow=(r"mieszkanie/wynajme/*[a-z]*(\?PageNumber=[0-9]*)*$"))),
	)