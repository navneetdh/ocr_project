from confluent_kafka import Consumer, KafkaException
import json
from config.settings import KAFKA_BROKER, KAFKA_TOPIC
from ocr_engine.ocr_processor import process_task
from utils.logger import logger

def consume_ocr_tasks():
    conf = {
        'bootstrap.servers': KAFKA_BROKER,
        'group.id': 'ocr_group',
        'auto.offset.reset': 'earliest'
    }

    consumer = Consumer(conf)
    consumer.subscribe([KAFKA_TOPIC])

    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    logger.error(f"Kafka error: {msg.error()}")
                    break

            task = json.loads(msg.value().decode('utf-8'))
            file_path = task.get('file_path')
            if file_path:
                process_task(file_path)
            else:
                logger.error("Received task without file_path")

    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()