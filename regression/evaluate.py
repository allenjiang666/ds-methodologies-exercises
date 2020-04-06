import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from statsmodels.formula.api import ols

def plot_residuals(y, yhat):
    residuals = y - yhat
    plt.scatter(y_hat, residuals)
    
from sklearn.metrics import mean_squared_error
from math import sqrt

def regression_errors(y, y_hat):
    MSE = mean_squared_error(y, y_hat)
    SSE = mean_squared_error(y, y_hat)*len(y)
    RMSE = sqrt(mean_squared_error(y, y_hat))
    ESS = sum((y_hat - y.mean())**2)
    TSS = SSE + ESS
    return SSE, ESS, TSS, MSE, RMSE

def baseline_mean_errors(y):
    y_bl = df.y + df.y.mean() -df.y
    SSE = mean_squared_error(y, y_bl)*len(y)
    MSE = mean_squared_error(y, y_bl)
    RMSE = sqrt(mean_squared_error(y, y_bl))
    return SSE, MSE, RMSE

def better_than_baseline(y, yhat):
    y_bl = y + y.mean() - y
    RMSE_bl = sqrt(mean_squared_error(y, y_bl))
    RMSE = sqrt(mean_squared_error(y, df.y_hat))
    return RMSE < RMSE_bl

def model_significance(ols_model):
    r2 = ols_model.rsquared
    p_val = ols_models.f_pvalue
    return r2, p_val