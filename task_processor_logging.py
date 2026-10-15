import logging
from logging.handlers import RotatingFileHandler


# Agent Task Processor with Fully Logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)

file_handler = RotatingFileHandler("Task_processor.log", maxBytes = 1000, backupCount = 2)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Create Function

def process_task(task_name,priority):
    logger.info('Processing Task : %s',task_name)
    try:
        if priority > 10:
            logger.warning('Priority too high ,capping at 10')
            priority = 10

        elif priority < 0:
             logger.warning('Negative priority, setting to 0')
             priority =0   

             logger.info('Task %s  completed with priority %s ',task_name,priority)
             return priority
    except TypeError as e:
        logger.error('Invalid priority type %s', e,exc_info= True) 
        return None   


process_task("send_email", 5)
process_task("fetch_data", 15)
process_task("Cleanup", -3)
process_task("backup_dp", "high")
process_task("generate_report", 8)