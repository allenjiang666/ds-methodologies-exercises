import pandas as pd
import requests

def get_data(table_name):
    response = requests.get('https://python.zach.lol/api/v1/'+ table_name)
    data = response.json()
    df = pd.DataFrame(data['payload'][table_name])
    base_url = 'https://python.zach.lol'
    while data['payload']['next_page'] != None:
        response = requests.get(base_url + data['payload']['next_page'])
        data = response.json()
        df = pd.concat([df, pd.DataFrame(data['payload'][table_name])])
    df = df.reset_index(drop = True)
    return df

def save_flies(table_name: str):
    get_data(table_name).to_csv(table_name + '.csv')
    
def get_sales_info():
    items = pd.read_csv('items.csv', index_col= 0)
    stores = pd.read_csv('stores.csv', index_col= 0)
    sales = pd.read_csv('sales.csv', index_col= 0)
    sales_info = pd.merge(sales, items, left_on='item', right_on='item_id', how='left')
    sales_info = pd.merge(stores, sales_info, left_on='store_id', right_on='store', how='left')
    return sales_info