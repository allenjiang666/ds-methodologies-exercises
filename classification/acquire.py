import pandas as pd
from env import url
def get_titanic_data():
    query ='''
        Select * from passengers
    '''
    df = pd.read_sql(query, url('titanic_db'))
    return df

def get_iris_data():
    query = '''SELECT *
    FROM measurements
    JOIN species USING(species_id)'''
    df = pd.read_sql(query, url('iris_db'))
    return df