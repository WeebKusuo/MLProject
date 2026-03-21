## main aim of this --FEature Engg and data cleaning and convert the cat feature to num features etc 
import sys 
from dataclasses import dataclass
import numpy as np 
import pandas as pd 
from sklearn.compose import ColumnTransformer
from src.logger import logging
from src.exception import CustomException
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder,StandardScaler
import os 
from src.utlis import save_object


@dataclass #-- what it does yeh basically ek class ko simple bna deta hai jahan bhi data store krna ho python automatically  __init__ bna deta hai 
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts',"preprocessor.pkl")


class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()

    def get_Data_transformer_object(self):
        #this function is responsible for transformation of different types of data
        try:
            numeric_columns=['writing score','reading score']
            categorical_columns=[
                "gender",
                "race/ethnicity",
                "parental level of education",
                "lunch",
                "test preparation course",
            ]

            num_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="median")),
                    ("scaler",StandardScaler())
                ]
            )

            logging.info("Numerical Columns Standard Scaling Completed")

            cat_pipeline=Pipeline(
                steps=[
                    ("imputer",SimpleImputer(strategy="most_frequent")),
                    ("onehot",OneHotEncoder()),
                    ("scaler",StandardScaler(with_mean=False))  #"OneHotEncoder ke baad StandardScaler use karte waqt with_mean=False lagana padta hai"
                ]
            )
            logging.info("Categorical Columns Encoding Completed")

            preprocessor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numeric_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                ]
            )
            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
                  
    def iniciate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)
            logging.info("Reading of train&test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj=self.get_Data_transformer_object()

            target_Column_name='math score'
            numeric_columns=['writing score','reading score']


            input_feature_train_df=train_df.drop(columns=[target_Column_name],axis=1)
            target_feature_train_df=train_df[target_Column_name]

            input_feature_test_df=test_df.drop(columns=[target_Column_name],axis=1)
            target_feature_test_df=test_df[target_Column_name]

            logging.info(
                "Applying the preprocessing object on training and testing dataframes "
            )
            #preprocessing sirf inout feature par hi lagti hai 
            input_feature_train_arr=preprocessing_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_feature_test_df)

            # what does np.c_ do Arrays ko column-wise join (side by side) karta hai
            train_arr=np.c_[
                input_feature_train_arr,np.array(target_feature_train_df)
            ]


            test_arr=np.c_[
                input_feature_test_arr,np.array(target_feature_test_df)
            ]

            logging.info("Saved preprocessing objects")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj=preprocessing_obj
            )
            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path,

            )



        except Exception as e:
            raise CustomException(e,sys)
            
