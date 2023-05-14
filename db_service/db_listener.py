"""Rabbit listener"""
import json
import sys
import os
from time import sleep

from kafka import KafkaConsumer


def main():
    # consumer
    topic = 'second_topic'
    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'], auto_offset_reset='earliest',
                             value_deserializer=lambda x: json.loads(x.decode('utf-8')))


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)