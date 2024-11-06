from typing import Tuple
import pandas as pd
from pathlib import Path
import xgboost as xgb
import catboost as cat
from lib.utils import *



if __name__ == '__main__':
    path_data = Path("")
    trainset, testset = load_processed_datasets(path_data)
    model = setup_model("xgboost", hyperparameters={})
    
            
    model.fit(trainset)
    model.predict(testset)
    