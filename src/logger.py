import logging
import os
from datetime import datetime

'''
    %d_%m_%Y_%H_%M_%S == day, month, year, hour, minute, seconds
'''

LOG_FILE = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"
logs_dir = os.path.join(os.getcwd(),"logs")
os.makedirs(logs_dir,exist_ok=True)

LOGS_FILE_PATH = os.path.join(logs_dir,LOG_FILE)
logging.basicConfig(
    filename=LOGS_FILE_PATH,
    format="%(asctime)s - %(lineno)d - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
) 

