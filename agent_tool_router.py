import logging

# Task-Agentic tool  Router with ERROR Fallback

# logging configuration
logging.basicConfig(
    filename="agent_router.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
    force=True
)

def primary_calculator(a:float,b:float)->float:
    return a/b

def fallback_calculator(a:float,b:float)->float:
    return a+b

def run_agent_router(a:float,b:float)->None:
    try:
        logging.info("Mathmatical task processing")
        result = primary_calculator(a,b)
        print(f"primary result is:{result}")
        
    except Exception as e:
        logging.error("Task failed:",exc_info=True)
        logging.warning("Switching to fallback (Adition)")

        result=fallback_calculator(a,b)
        print(f"Fallback result:{result}")
    finally:
        logging.info("AI Agent finished") 
if __name__ == "__main__":
    run_agent_router(10,0)           