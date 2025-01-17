import logging
import os
from datetime import datetime

Log_File = f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

Log_Path = os.path.join(os.getcwd(),"LOGS",Log_File) #cwd = current working directory

os.makedirs(Log_Path,exist_ok=True) #exist_ok is used to append in folder logs 

Log_File_Path = os.path.join(Log_Path,Log_File)

logging.basicConfig(
    filename = Log_File_Path,
    format = "[%(asctime)s ] %(lineno)d  %(name)s  -  %(levelname)s - %(message)s",
    level= logging.INFO,
)

if __name__ == "__main__" :
    logging.info(" Mayuri Has logging started ") 

# to call this file write == python src/logger.py