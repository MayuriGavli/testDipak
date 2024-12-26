import sys
import os
from src import logging
from src import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # create class variable

@dataclass  #decorator ----(call)define your class variable
#this below class is used to give any input which is required anywhere as input
#Data Ingestion is used to read data from other location
class DataIngestionconfig:
    train_data_path : str = os.path.join("artifacts","train.csv")  #this is input giving to my data ingestion component and now data ingestion component where to store train and test data
    test_data_path : str = os.path.join("artifacts","test.csv")
    raw_data_path : str = os.path.join("artifacts","data.csv")

    #all above are class variable

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionconfig()

    def initiate_data_ingestion(self):
        df = pd.read_csv("Notebook/Dataset/students.csv")
        logging.info("Entered the data ingestion method and components")

        try:
            logging.info("Reading the dataset as dataframe")
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path)exist_ok=True)














