import logging
import os
from datetime import datetime

# format of the file 
LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# name of the file
logs_path=os.path.join(os.getcwd(),"logs",LOG_FILE)

#even if there is a file or folder keep on appending them to the same
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

#logging setup
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# if __name__=="__main__":
#     logging.info("Logging has started")

    

