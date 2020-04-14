import pandas as pd
import pydataset

def get_titanic_data():
    df = pydataset.data('titanic')
    return df

def get_iris_data():
    df = pydataset.data('iris')
    return df