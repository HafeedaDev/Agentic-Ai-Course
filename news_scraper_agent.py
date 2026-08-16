import logging

# task- News scraper Agent with Fallback

# logging configuration
logging.basicConfig(
    filename="news_agent.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    force=True
)

def primary_news_source(topic:str) ->str:
    raise ConnectionError("Failed to connect to server")

def backup_news_source(topic: str)-> str:
    return "Connected beckup server"

def fetch_news_agent(topic: str)->None:
    try:
        logging.info("Processing news scraper agent")
        result = primary_news_source(topic)
        print(f"primary task:{result}")
    except Exception as e:
        logging.error("Failed Task:",exc_info=True)
        logging.warning("System Switched to backup")

        result = backup_news_source(topic)
        print(f"Result is :{result}")

    finally:
        logging.info("News fetching  process completed")
if __name__ == "__main__":
    fetch_news_agent("AI Agent")           