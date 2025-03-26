import logging
import os

# Ensure log directory exists
LOG_DIR = "log"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Configure logging
LOG_FILE = os.path.join(LOG_DIR, "app.log")
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

def log_event(event_type, message):
    """
    Log an event with different severity levels.
    
    :param event_type: "info", "warning", "error"
    :param message: The log message
    """
    if event_type == "info":
        logging.info(message)
    elif event_type == "warning":
        logging.warning(message)
    elif event_type == "error":
        logging.error(message)

# Example Usage
if __name__ == "__main__":
    log_event("info", "Application started.")
    log_event("warning", "Low memory warning.")
    log_event("error", "Deadlock detected!")
