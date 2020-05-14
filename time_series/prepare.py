import pandas as pd
from acquire import get_store_data
from datetime import timedelta, datetime
import numpy as np

def prepare_store_data(): 
    df = get_store_data().drop(columns = ['store_id','item_id'])
    # Reassign the sale_date column to be a datetime type
    df['sale_date'] = pd.to_datetime(df['sale_date'])
    # Sort rows by the date and then set the index as that date
    df = df.sort_values("sale_date").set_index("sale_date")
    # Add a 'month' and 'day of week' column
    df['month'] = df.index.month_name()
    df['day_of_week'] = df.index.day_name()
    # Add a column sales_total
    df['sales_total'] = df.sale_amount * df.item_price
    # create a new column current sales - the previous days sales
    df["diff(1)"] = df.sales_total.diff(1)
    return df

def prepare_ops_data():
    ops =pd.read_csv('https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv')
    #onvert date column to datetime format
    ops['Date'] = pd.to_datetime(ops['Date'])
    #Set the index to be the datetime variable.
    ops = ops.sort_values("Date").set_index("Date")
    #Add a month and a year column to your dataframe
    ops['month'] = ops.index.month
    ops['year'] = ops.index.year
    return ops