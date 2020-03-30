#Acquisition and Prep
import pandas as pd
import numpy as np


def wrangle_telco():
    url = url("telco_churn")
    sql = '''SELECT customer_id, monthly_charges, tenure, total_charges 
    FROM customers
    WHERE contract_type_id = 3'''
    df = pd.read_sql(sql, url)
    df.total_charges = df.total_charges.str.strip()
    df = df[df.total_charges != '']
    df.total_charges = df.total_charges.astype('float')
    return df