# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json


from itemadapter import ItemAdapter
import pika
import json
from datetime import datetime
from time import sleep
from random import choice
from confluent_kafka import Producer
from faker import Faker
import json
import time
import random

from kafka import KafkaProducer


class FlatcrawlingPipeline:
    connection = None
    channel = None
    producer = None

    def open_spider(self, spider):
        self.producer = KafkaProducer(bootstrap_servers='kafka:29092', max_block_ms=10000)

    def close_spider(self, spider):
        self.producer.close()
        pass

    def process_item(self, item, spider):
        self.producer.send(json.dumps(item))
