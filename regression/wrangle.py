#Acquisition and Prep
import pandas as pd
import numpy as np
from env import url


def wrangle_telco():
    sql = '''SELECT customer_id, monthly_charges, tenure, total_charges 
    FROM customers
    WHERE contract_type_id = 3'''
    df = pd.read_sql(sql, url("telco_churn"))
    df.total_charges = df.total_charges.str.strip()
    df = df[df.total_charges != '']
    df.total_charges = df.total_charges.astype('float')
    return df