import sys
import os
from src.logger import logging
from src.exception import CustomException
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass # used to create class variable

@dataclass  #decorator ----(call)define your class variable
#this below class is used to give any input which is required anywhere as input
#Data Ingestion is used to read data from other location like from API or otherelse 
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

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,header=True,index=False) 
            #header=True This ensures that the column names of the DataFrame are included as the first row (header) in the CSV file.
            #index=False an additional column with index numbers would be included in the CSV.

            logging.info("train and test split initiated")

            train_set,test_set = train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,header=True,index=False)

            test_set.to_csv(self.ingestion_config.test_data_path,header=True,index=False)

            logging.info("Ingestion of data completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e,sys)



if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()


# to run = python src/components/data_ingestion.py











