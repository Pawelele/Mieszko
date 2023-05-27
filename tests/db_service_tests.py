"""Module contains mocked data to check correctness of working the db_service"""
import unittest

import mysql.connector
from confluent_kafka import Consumer
from kafka import KafkaProducer

from db_service.src.db_actions import Database


class TestDatabaseMethods(unittest.TestCase):
#cqrs
	def test_singleton(self):
		db_connection = Database()
		second_connection = Database()

		self.assertIs(db_connection, second_connection)

	def test_connection(self):
		connection = mysql.connector.connect(
			user='root', password='root', host='localhost', port=3306, database="offers"
		)
		self.assertIsNotNone(connection)


class TestQueueMethods(unittest.TestCase):

	def test_consumer_connection(self):

		conf = {
				'bootstrap.servers': 'localhost:9092',
				'group.id': 'my-consumer-group',
				'auto.offset.reset': 'earliest'
			}

		consumer = Consumer(conf)
		topic = 'db_topic'
		consumer.subscribe([topic])

		msg = consumer.poll(1.0)
		self.assertIsNotNone(msg)

	def test_producer_connection(self):
		producer = KafkaProducer(bootstrap_servers='kafka:29092', max_block_ms=10000)
		self.assertIsNotNone(producer)
