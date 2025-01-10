from exordium import get_logger
import time
import random

logger = get_logger(__name__)

def simulate_events():
    events = ['DEBUG', 'INFO', 'SUCCESS', 'WARNING', 'ERROR', 'CRITICAL']
    messages = [
        "Processing data",
        "User logged in",
        "Operation completed successfully",
        "Disk space is low",
        "Failed to connect to database",
        "System crash imminent"
    ]

    while True:
        event = random.choice(events)
        message = random.choice(messages)
        
        if event == 'DEBUG':
            logger.debug(message)
        elif event == 'INFO':
            logger.info(message)
        elif event == 'SUCCESS':
            logger.success(message)
        elif event == 'WARNING':
            logger.warning(message)
        elif event == 'ERROR':
            logger.error(message)
        elif event == 'CRITICAL':
            logger.critical(message)
        
        time.sleep(random.uniform(0.5, 2))

if __name__ == "__main__":
    simulate_events()