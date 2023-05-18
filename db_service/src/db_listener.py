"""Rabbit listener"""
import json
import sys
import os
from time import sleep

from kafka import KafkaConsumer

import logging

# Configure the logging module
logging.basicConfig(level=logging.INFO)

# Create a logger instance
logger = logging.getLogger(__name__)

sleep(10)

consumer = KafkaConsumer(
    'db_topic',
    bootstrap_servers=['kafka:9092'],
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for message in consumer:
    # Log the received message
    logger.info(f"Received message: {message}")

# def main():
#     # consumer
#     conf = {
#         'bootstrap.servers': '127.0.0.1:9092',  # Adresy serwerów Kafka
#         'group.id': 'my-consumer-group',  # Identyfikator grupy konsumentów
#         'auto.offset.reset': 'earliest'  # Ustawienie początkowego offsetu na najstarszy dostępny
#     }

#     # Utworzenie obiektu konsumenta
#     consumer = Consumer(conf)

#     # Subskrypcja do tematu
#     topic = 'second_topic'
#     consumer.subscribe([topic])

#     # Pętla odbierająca wiadomości
#     while True:
#         msg = consumer.poll(1.0)  # Oczekiwanie na wiadomość przez 1 sekundę

#         if msg is None:
#             continue
#         if msg.error():
#             print(f"Błąd odbierania wiadomości: {msg.error()}")
#             continue

#         # Przetwarzanie odebranej wiadomości
#         print(f"Odebrano wiadomość: {msg.value().decode('utf-8')}")

#     # Zamknięcie konsumenta
#     consumer.close()

# if __name__ == '__main__':
#     try:
#         main()
#     except KeyboardInterrupt:
#         print('Interrupted')
#         try:
#             sys.exit(0)
#         except SystemExit:
#             os._exit(0)