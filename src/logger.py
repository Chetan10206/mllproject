#Logger = records everything happening
#Exception = explains what went wrong

import logging
import os
from datetime import datetime 

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # create log file name
logs_path= os.path.join(os.getcwd(),'logs') # Create logs folder  , os.getcwd() is current working directly
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE) #Final log file path
 
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

if __name__=="__main__": # to check is it working
    logging.info("logging has started")
