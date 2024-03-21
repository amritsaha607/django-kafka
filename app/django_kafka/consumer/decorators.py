import sys
import traceback

from confluent_kafka import KafkaError, KafkaException
from django.conf import settings

from .consumer import get_kafka_consumer_from_config


def handle_exception(function):
    """
    A decorator to catch & log exception
    """
    def wrapper(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception as e:
            print(
                f"Error in kafka consumer : {traceback.format_exc()}")

    return wrapper


def kafka_listener(function):

    @handle_exception
    def validate_message(message):

        if message is None:
            return False

        if message.error():

            if message.error().code() == KafkaError._PARTITION_EOF:
                sys.stderr.write('%% %s [%d] reached end at offset %d\n' %
                                 (message.topic(), message.partition(), message.offset()))
                return False

            elif message.error():
                raise KafkaException(message.error())

        return True

    def wrapper(*args, **kwargs):
        consumer = get_kafka_consumer_from_config()

        try:
            consumer.subscribe(settings.KAFKA_TOPIC_NAMES)
            print(
                f"Successfully subscribed kafka consumer to topic {settings.KAFKA_TOPIC_NAMES}")

            while True:
                message = consumer.poll(0)
                if not validate_message(message):
                    continue

                function_handled = handle_exception(function)
                function_handled(message, *args, **kwargs)

        finally:
            consumer.close()

    return wrapper
