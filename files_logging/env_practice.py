import os
import logging
from dotenv import load_dotenv

# Task Name: Environment Variable Integration & Secure Credentials Management
# ----------------------------------------------------------------------------

def initialize_env():

# 1. logging configuration
    logging.basicConfig(
    filename="news_agent.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    force=True
    )

 # 2.opening .env file
    load_dotenv()

#  take Api key
    api_key = os.getenv("MY_AGENT_API_KEY")

# 4. Checking whether the key has been received or not
    if api_key is None:
        logging.error("API Key not found")
        print("API Key not found")
    else:
        logging.info("API Key loaded successfully")
        print(f"API Key found: ****{api_key[-4:]}")

if __name__ == "__main__":
    initialize_env()