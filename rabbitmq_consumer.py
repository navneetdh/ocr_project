import pika
import json
import os
from settings import RABBITMQ_HOST, QUEUE_NAME, INPUT_DIR, OUTPUT_DIR
from ocr_processor import process_task
from logger import logger

def consume_ocr_tasks():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)

    def callback(ch, method, properties, body):
        task = json.loads(body.decode('utf-8'))
        file_path = task.get('file_path')
        if file_path:
            process_task(file_path, OUTPUT_DIR)
            ch.basic_ack(delivery_tag=method.delivery_tag)
        else:
            logger.error("Received task without file_path")
            ch.basic_nack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=QUEUE_NAME, on_message_callback=callback)

    logger.info('Waiting for messages. To exit press CTRL+C')
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    finally:
        connection.close()

if __name__ == '__main__':
    consume_ocr_tasks()