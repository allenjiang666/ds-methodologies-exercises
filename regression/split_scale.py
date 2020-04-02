import pandas as pd 
import numpy as np
from sklearn.preprocessing import StandardScaler, QuantileTransformer, PowerTransformer, RobustScaler, MinMaxScaler

def split_my_data(X, y, train_pct):
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=train_pct, random_state=123)
    return X_train, X_test, y_train, y_test

def standard_scaler(train, test):
    #grab dataframe column names
    columns = train.columns
    #make a copy of original
    train_scaled = train.copy()
    test_scaled = test.copy()
    #create a scaler
    scaler = StandardScaler()
    #fit scaler
    scaler.fit(train)
    #aplly the scaler to train and test dataset
    train_scaled[columns] = scaler.transform(train)
    test_scaled[columns] = scaler.transform(test)
    return train_scaled, test_scaled, scaler

def scale_inverse(train_scaled, test_scaled, scaler):
    train = pd.DataFrame(scaler.inverse_transform(train_scaled), columns=train_scaled.columns, index=train_scaled.index)
    test = pd.DataFrame(scaler.inverse_transform(test_scaled), columns=test_scaled.columns, index=test_scaled.index)
    return train, test

def uniform_scaler(train, test):
    scaler = QuantileTransformer(n_quantiles=100, output_distribution='uniform', random_state=123, copy=True).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns, index=test.index)
    return train_scaled, test_scaled, scaler

def gaussian_scaler(train, test):
    scaler = PowerTransformer(method='yeo-johnson', standardize=False, copy=True).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return train_scaled, test_scaled, scaler

def min_max_scaler(train, test):
    scaler = MinMaxScaler(copy=True, feature_range=(0,1)).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values]) 
    return train_scaled, test_scaled, scaler

def iqr_robust_scaler(train, test):
    scaler = RobustScaler(quantile_range=(25.0,75.0), copy=True, with_centering=True, with_scaling=True).fit(train)
    train_scaled = pd.DataFrame(scaler.transform(train), columns=train.columns.values).set_index([train.index.values])
    test_scaled = pd.DataFrame(scaler.transform(test), columns=test.columns.values).set_index([test.index.values])
    return train_scaled, test_scaled, scaler