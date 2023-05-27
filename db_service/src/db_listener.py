"""Rabbit listener"""
import json
import sys
import os
from time import sleep

from kafka import KafkaConsumer

import logging

# Configure the logging module
from db_service.src.db_actions import Database

logging.basicConfig(level=logging.INFO)

# Create a logger instance
logger = logging.getLogger(__name__)

sleep(100)

consumer = KafkaConsumer(
    'db_topic',
    bootstrap_servers=['kafka:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

db = Database()
for message in consumer:
    # Log the received message
    logger.info(f"Received message: {message}")
