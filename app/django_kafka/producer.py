from confluent_kafka import Producer
from django.conf import settings


def get_kafka_producer_from_config():
    producer_conf = {
        'bootstrap.servers': settings.KAFKA_BOOTSTAP_SERVER,
        'client.id': settings.KAFKA_CLIENT_ID,
    }

    producer = Producer(producer_conf)

    return producer
