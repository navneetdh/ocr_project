import pika
import json
import os
from settings import RABBITMQ_HOST, QUEUE_NAME, INPUT_DIR
from logger import logger

def produce_ocr_tasks():
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST))
    channel = connection.channel()
    channel.queue_declare(queue=QUEUE_NAME, durable=True)
    
    for filename in os.listdir(INPUT_DIR):
        file_path = os.path.join(INPUT_DIR, filename)
        if os.path.isfile(file_path) and filename.lower().endswith(('png', 'jpg', 'jpeg', 'tiff', 'bmp', 'gif')):
            task = {'file_path': file_path}
            channel.basic_publish(exchange='', routing_key=QUEUE_NAME, body=json.dumps(task))
            logger.info(f"Sent task for file: {file_path}")
    
    connection.close()

if __name__ == '__main__':
    produce_ocr_tasks()