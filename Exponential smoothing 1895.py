# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 15:40:06 2020

@author: Dell
"""

import numpy as np
import pandas as pd
import datetime

data_1 = pd.read_csv(r"C:\Users\Dell\Desktop\New folder\Deposco\more_than_200\data_1895.csv")
data = data_1.copy()
data.timestamp= pd.to_datetime(data.timestamp,dayfirst=True) 
data.set_index('timestamp',inplace=True)
type(data)
del data['Unnamed: 0']

data=data.asfreq(freq='d')
data.isna().sum()
data.item_id=data.item_id.fillna(method='ffill')
data.demand=data.demand.fillna(method='ffill')
data.isna().sum()
data.demand.plot()


from statsmodels.tsa.holtwinters import ExponentialSmoothing

data['DESmul30'] = ExponentialSmoothing(data['demand'], trend='mul').fit().fittedvalues.shift(-1)
data['TESadd30'] = ExponentialSmoothing(data['demand'],trend='add',seasonal='add',seasonal_periods=30).fit().fittedvalues
data['TESmul30'] = ExponentialSmoothing(data['demand'],trend='mul',seasonal='mul',seasonal_periods=30).fit().fittedvalues
data[['demand','DESmul30','TESmul30','TESadd30']].iloc[180:].plot(figsize=(12,3)).autoscale(axis='x',tight=True);