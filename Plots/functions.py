#%%
import pandas as pd
from IPython.core.display_functions import display


def print_maxima(df):
    pd.set_option('display.max_colwidth', None)
    
    all_dates = pd.date_range(start=df['days'].min(), end=df['days'].max())
    columns = df.columns[1: len(df.columns)-1]
    x_values_per_day = df.groupby('days', dropna=False)[columns].agg(lambda x: x.sum(skipna=False))
    x_values_per_day = x_values_per_day.reindex(all_dates, fill_value=None)
    
    maxima = x_values_per_day.idxmax()
    print(maxima)
#%%
def print_null_values(df):
    all_dates = pd.date_range(start=df['days'].min(), end=df['days'].max())
    columns = df.columns[1: len(df.columns) - 1]
    x_values_per_day = df.groupby('days', dropna=False)[columns].agg(lambda x: x.sum(skipna=False))
    x_values_per_day = x_values_per_day.reindex(all_dates, fill_value=None)
    pd.set_option('display.max_colwidth', None)
    null_mask = x_values_per_day.isnull().any(axis=1)
    null_rows = x_values_per_day[null_mask]
    length = len(x_values_per_day.columns)
    keys = x_values_per_day.columns[1:length - 1]
    nulls = []
    groups = df.groupby('days')
    for column in keys:
        print(column)
        null_crossings = []
        values = [name for name, gruppe in groups if gruppe[column].isnull().all()]
        null_crossings.append(column)
        null_crossings.append(values)
        nulls.append(null_crossings)
    display(nulls)
#%%
def print_zeros(df, values):
    all_dates = pd.date_range(start=df['days'].min(), end=df['days'].max())
    columns = df.columns[1: len(df.columns) - 1]
    x_values_per_day = df.groupby('days', dropna=False)[columns].agg(lambda x: x.sum(skipna=False))
    x_values_per_day = x_values_per_day.reindex(all_dates, fill_value=None)
    length=len(x_values_per_day.columns)
    keys= x_values_per_day.columns[1:length-1]
    #cols = (x_values_per_day == 0).any()
    #zero_days = x_values_per_day.loc[:,cols]
    zeros = []
    groups = df.groupby('days')
    
    for column in keys:
        zero_crossings = []
        cols = (x_values_per_day[column] == 0)
        values = [name for name, gruppe in groups if (gruppe[column] == 0).all()]
        zero_crossings.append(column)
        zero_crossings.append(values)
        zeros.append(zero_crossings)
    print(zeros)