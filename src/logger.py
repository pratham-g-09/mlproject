import logging
import os
from datetime import datetime

# Generate timestamp for logs
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"  # Added '.log' for clarity
logs_path = os.path.join(os.getcwd(), "logs")  # Directory for logs
os.makedirs(logs_path, exist_ok=True)

# Full path for the log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# Logging configuration
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


