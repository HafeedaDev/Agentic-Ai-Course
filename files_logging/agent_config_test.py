import os
import logging
from dotenv import load_dotenv

def agent_config():
    # 1. logging configuration
    logging.basicConfig(
    filename="agent_system.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    force=True
    )

    # 2 open env file
    load_dotenv()

    3 #  take Api key
    agent_name = os.getenv("AGENT_NAME")
    agent_token = os.getenv("AGENT_SECRET_TOKEN")

    if  not agent_name or not agent_token:
         logging.error("Configuration missing!")  
         print(f"Configuration missing!")
         
    else :
        logging.info(f"Agent {agent_name} configured with valid token")
        print(f"Successful! Got Agent  {agent_name} ,Token ****{agent_token[-4:]}")
        

if __name__ == "__main__":
      agent_config()