import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from ocr_processor import process_task
from logger import logger

class NewFileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            logger.info(f"New file detected: {event.src_path}")
            process_task(event.src_path)

def monitor_directory(directory_path):
    event_handler = NewFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory_path, recursive=False)
    observer.start()
    logger.info(f"Started monitoring directory: {directory_path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_directory('/path/to/watch')