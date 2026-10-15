import logging
from operator import le

logging.basicConfig(
   filename="logging_file.log",
   filemode= "a",
   format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO,
   force=True
)

def account_withdraw(account_balance,amount):
    logging.info(f"Starting account withdrawal process {account_balance}")
    try:
      
      if amount > account_balance:
       logging.warning("Insufficient balance")
    
       return account_balance
      else:
        balance = account_balance-amount
        logging.info(f"Successfully Completed Withdrawal.Your account balance is: {balance}")
        return balance
    except TypeError as e:
        logging.error(f"Invalid Input {e}",exc_info=True)
        return None

    except Exception as e:
        logging.error(f"Got Unexcepted error: %s ", e,exc_info=True)   
        return None
account_withdraw(5000,"hundred")        




































