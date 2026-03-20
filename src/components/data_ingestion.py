# plays a very important role
# as ml engg or data scientist we need to read data from different types of sources like mongodb etc
# like first we will read the data 
# main aim is to read the dataset from a data source and split the data 

import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass


@dataclass
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts',"train.csv")
    test_data_path: str=os.path.join('artifacts',"test.csv")
    raw_data_path: str=os.path.join('artifacts',"data.csv")



# # 📌 Data Ingestion Config – Quick Notes (ML Project)

# ## 🔹 1. `@dataclass` kya hai?

# * Python decorator hai
# * Class ko simple bana deta hai
# * Automatically `__init__()` create karta hai
# * Mainly **data store karne ke liye use hota hai**

# ---

# ## 🔹 2. DataIngestionConfig ka purpose

# * Ye ek **configuration class** hai
# * Sirf **file paths (addresses)** store karti hai
# * Data store nahi karti ❌

# ---

# ## 🔹 3. Code Understanding

# ```python
# @dataclass
# class DataIngestionConfig:
#     train_data_path: str = os.path.join('artifacts', "train.csv")
#     test_data_path: str = os.path.join('artifacts', "test.csv")
#     raw_data_path: str = os.path.join('artifacts', "data.csv")
# ```

# ### 👉 Iska matlab:

# * Train data → `artifacts/train.csv`
# * Test data → `artifacts/test.csv`
# * Raw data → `artifacts/data.csv`

# ---

# ## 🔹 4. `os.path.join()` kyun use kiya?

# * Cross-platform compatibility (Windows/Linux/Mac)
# * Automatically correct path banata hai
# * Best practice ✅

# ---

# ## 🔹 5. Important Concept ⚠️

# 👉 Ye class:

# * ❌ File create nahi karti
# * ❌ Data save nahi karti

# 👉 Ye sirf batati hai:

# > "File ko kaha save karna hai"

# ---

# ## 🔹 6. Actual Data Saving kaha hoti hai?

# ```python
# df.to_csv(config.train_data_path)
# ```

# 👉 Yaha:

# * File create hoti hai
# * Data save hota hai ✅

# ---

# ## 🔹 7. Flow of Data Ingestion

# 1. Config class → paths define karti hai
# 2. Data read hota hai (CSV etc.)
# 3. Train-test split hota hai
# 4. Data save hota hai using config paths

# ---

# ## 🔹 8. Real-life analogy 🧠

# * Config = Address 📍
# * Data Ingestion = Delivery 🚚

# > Address already set hai, bas data waha deliver karna hai

# ---

# ## 🔹 9. Benefits (Interview Points)

# * Clean code ✅
# * No hardcoding ✅
# * Easy to modify paths ✅
# * Industry standard (MLOps) ✅

# ---

# ## 🔥 Final One-line

# > "DataIngestionConfig stores file paths, while actual data saving is handled in the Data Ingestion logic."

# ---


class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

# DataIngestionConfig() paths define karta hai (batata hai ki file kaha save hogi).
# Phir DataIngestion class ke andar hum uska object bana ke un paths ko store kar lete hain, taaki hum unhe easily use/access kar saken.
# DataIngestionConfig()
# Paths define karta hai
# like train → artifacts/train.csv

# DataIngestion class
# self.ingestion_config = DataIngestionConfig()

# 👉 Iska matlab:
# "Jo paths config me defined hain, unko le aao aur mere paas rakh do"


# 3. Ab use kaise hoga?
# self.ingestion_config.train_data_path

# 👉 Direct access mil gaya
# like output hoga Output milega:

# artifacts/train.csv

    def iniciate_data_ingestion(self):
        logging.info("entered the data ingestion method or component")
        try:
            df=pd.read_csv('notebook\data\StudentsPerformance.csv')
            logging.info('Read the dataset as DataFrame')
            #  here we are making the folder of artifacts like os.makedirs ke pbaad jo toh os.path.dirname hai na woh pure path se folder ka name lega 
            #  cause hamare pass full path hai which includes both folder and file path humne folder path chahiye isliye humne ese kra
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            # artifacts folder ke andar data.csv file create hogi + data save hoga

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)

            logging.info("Train Test Split iniciated")

            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)

            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Ingestion of the data is Completed ")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys)
        

if __name__=="__main__":
    obj=DataIngestion()
    obj.iniciate_data_ingestion()        
