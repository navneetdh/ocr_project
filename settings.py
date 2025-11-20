import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'postgresql://yourusername:yourpassword@localhost/ocr_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
KAFKA_BROKER = 'localhost:9092'
KAFKA_TOPIC = 'ocr_tasks'
RABBITMQ_HOST = 'localhost'
QUEUE_NAME = 'ocr_tasks'
INPUT_DIR = "D:\Shared Folder\Courses\PROJECTS\OCR_PROJECT\word\Complete\\"
OUTPUT_DIR = "D:\Shared Folder\Courses\PROJECTS\OCR_PROJECT\Output\\'"
LOG_FILE = os.path.join(BASE_DIR, '../logs/ocr_system.log')