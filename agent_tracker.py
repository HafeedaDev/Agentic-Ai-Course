print("Success")
import logging

#logging configuration

logging.basicConfig(
    filename = "agent_trace.log",
    filemode = "a",
    format = "%(asctime)s - %(levelname)s - %(message)s",
    level = logging.INFO,
    force = True
)

def run_ai_agent() -> None:
    logging.info("AI Agent Started")
    try:
        logging.info("Processing Task")
        result = 10 / 0
    except Exception as e:
        logging.error("Task failed", exc_info=True)
    finally:
        logging.info("AI Agent Finished")
if __name__ == "__main__":
    run_ai_agent()        









