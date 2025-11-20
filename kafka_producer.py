from confluent_kafka import Producer
import json
from config.settings import KAFKA_BROKER, KAFKA_TOPIC
from utils.logger import logger
def delivery_report(err, msg):
    if err is not None:
        logger.error(f"Message delivery failed: {err}")
    else:
        logger.info(f"Message delivered to {msg.topic()} [{msg.partition()}]")

def produce_ocr_task(file_path):
    p = Producer({'bootstrap.servers': KAFKA_BROKER})
    task = {'file_path': file_path}
    p.produce(KAFKA_TOPIC, json.dumps(task).encode('utf-8'), callback=delivery_report)
    p.flush()