import os 
import sys

import numpy as np 
import pandas as pd
from src.exception import CustomException
import dill
# obj = jo bhi Python object tum save karna chahte ho (model, scaler, pipeline etc.)
def save_object(file_path, obj):
    try:
        # File path me se folder ka naam extract kiya
        dir_path = os.path.dirname(file_path)
        # Agar folder exist nahi karta toh create kar diya
        os.makedirs(dir_path, exist_ok=True)
        # File ko write binary mode me open kiya
        with open(file_path, "wb") as file_obj:
            # Object ko file ke andar save kar diya
            dill.dump(obj, file_obj)
            # file create hogi + preprocessor save ho jayega
    except Exception as e:
        raise CustomException(e, sys)