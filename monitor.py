import psutil
import time
from logger import logger

def log_system_metrics(interval=5):
    """
    Logs system metrics at specified intervals.

    Args:
        interval (int): Time in seconds between logging.
    """
    try:
        while True:
            cpu_usage = psutil.cpu_percent(interval=1)
            memory = psutil.virtual_memory()
            memory_usage = memory.percent
            logger.info(f"CPU Usage: {cpu_usage}% | Memory Usage: {memory_usage}%")
            time.sleep(interval - 1)
    except KeyboardInterrupt:
        logger.info("System monitoring stopped.")

if __name__ == "__main__":
    log_system_metrics()