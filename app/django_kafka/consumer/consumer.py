from confluent_kafka import Consumer
from django.conf import settings


def get_kafka_consumer_from_config():
    consumer_conf = {
        'bootstrap.servers': settings.KAFKA_BOOTSTAP_SERVER,
        'group.id': 'foo',
        # 'enable.auto.commit': 'false',
        # 'auto.offset.reset': 'earliest'
    }
    consumer = Consumer(consumer_conf)
    return consumer
