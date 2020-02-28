# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:52:29 2020

@author: Dell
"""

import pandas as pd
import matplotlib.pyplot as plt
import datetime

data_2 = pd.read_csv(r"C:\Users\Dell\Desktop\New folder\Deposco\more_than_200\data_1895.csv")
df = data_2.copy()
df.timestamp= pd.to_datetime(df.timestamp,dayfirst=True) 
df.set_index('timestamp',inplace=True)
type(df)
del df['Unnamed: 0']
del df['item_id']

df=df.asfreq(freq='d')
df.isna().sum()
df.demand=df.demand.fillna(method='ffill')
df.isna().sum()
df.demand.plot()

df.plot(grid = True)


import statsmodels.api as sm
decomp = sm.tsa.seasonal_decompose(df, model = 'additive')
decomp.plot()