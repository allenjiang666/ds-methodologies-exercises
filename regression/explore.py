# import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from wrangle import wrangle_telco

def plot_variable_pairs(dataframe):
    sns.pairplot(dataframe, kind='reg')
    plt.show()
    
def months_to_years(df):
    df.rename(columns = {'monthly_tenure': 'tenure_months'}, inplace = True)
    df["tenure_years"] = (df.tenure_months / 12).apply(np.ceil)
    return df

def plot_categorical_and_continous_vars(categorical_var, continuous_var, df):
    