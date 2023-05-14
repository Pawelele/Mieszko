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

fake=Faker()


class FlatcrawlingPipeline:
    connection = None
    channel = None

    def receipt(err, msg):
        if err is not None:
            print('Error: {}'.format(err))

    def open_spider(self, spider):
        # channel
        topic = 'second_topic'
        # producer
        producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                                 value_serializer=lambda x: json.dumps(x).encode('utf-8'))

    def close_spider(self, spider):
        pass

    def process_item(self, item, spider):
        for i in range(10):
            data = {
                'user_id': fake.random_int(min=20000, max=100000),
                'user_name': fake.name(),
                'user_address': fake.street_address() + ' | ' + fake.city() + ' | ' + fake.country_code(),
                'platform': random.choice(['Mobile', 'Laptop', 'Tablet']),
                'signup_at': str(fake.date_time_this_month())
            }
            m = json.dumps(data)
            self.p.poll(1)
            self.p.produce('user-tracker', m.encode('utf-8'), callback=self.receipt)
            self.p.flush()
            time.sleep(3)
