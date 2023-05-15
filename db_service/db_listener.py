"""Rabbit listener"""
import json
import sys
import os
from time import sleep

from confluent_kafka import Consumer
from kafka import KafkaConsumer


def main():
    # consumer
    conf = {
        'bootstrap.servers': '127.0.0.1:9092',  # Adresy serwerów Kafka
        'group.id': 'my-consumer-group',  # Identyfikator grupy konsumentów
        'auto.offset.reset': 'earliest'  # Ustawienie początkowego offsetu na najstarszy dostępny
    }

    # Utworzenie obiektu konsumenta
    consumer = Consumer(conf)

    # Subskrypcja do tematu
    topic = 'second_topic'
    consumer.subscribe([topic])

    # Pętla odbierająca wiadomości
    while True:
        msg = consumer.poll(1.0)  # Oczekiwanie na wiadomość przez 1 sekundę

        if msg is None:
            continue
        if msg.error():
            print(f"Błąd odbierania wiadomości: {msg.error()}")
            continue

        # Przetwarzanie odebranej wiadomości
        print(f"Odebrano wiadomość: {msg.value().decode('utf-8')}")

    # Zamknięcie konsumenta
    consumer.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)