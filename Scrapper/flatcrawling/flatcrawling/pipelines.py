# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter
import pika


class FlatcrawlingPipeline:
    connection = None
    channel = None

    def open_spider(self, spider):
        # MS TODO: OPEN CHANNEL
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='hello')

    def close_spider(self, spider):
        # MS TODO: CLOSE CHANNEL
        self.connection.close()

    def process_item(self, item, spider):
        # MS TODO: SEND DATA
        self.channel.basic_publish(exchange='',
                              routing_key='hello',
                              body=json.dumps(item))
        print(" [x] Sent 'Hello World!'")
