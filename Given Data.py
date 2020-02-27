# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:08:42 2020

@author: user
"""


import numpy as np
import pandas as pd
import datetime

data = pd.read_csv(r"C:\Users\Dell\Desktop\New folder\Deposco\demand.csv")
data.head()
len(data)
data.tail()
data.describe()
len(data['item_id'].unique())
unique_item_ids=data['item_id'].unique()
type(unique_item_ids)
dataset=[]

count_10=0
count_100=0
count_200=0
count_300=0
count_400=0
count_500=0
max_len=1
len_list=[]

for i,j in enumerate(unique_item_ids):
    df=data[data['item_id']==j]
    len_list.append(len(df))
    if len(df)<10:
        count_10=count_10+1
    if len(df)>500:
        count_500=count_500+1
        df.to_csv('C:/Users/Dell/Desktop/New folder/Deposco/more_than_500/'+'data'+'_'+str(i)+'.csv')
    elif len(df)>400:
        count_400=count_400+1
        df.to_csv('C:/Users/Dell/Desktop/New folder/Deposco/more_than_400/'+'data'+'_'+str(i)+'.csv')
    elif len(df)>300:
        count_300=count_300+1
        df.to_csv('C:/Users/Dell/Desktop/New folder/Deposco/more_than_300/'+'data'+'_'+str(i)+'.csv')
    elif len(df)>200:
        count_200=count_200+1
        df.to_csv('C:/Users/Dell/Desktop/New folder/Deposco/more_than_200/'+'data'+'_'+str(i)+'.csv')
    elif len(df)>100:
        count_100=count_100+1
        df.to_csv('C:/Users/Dell/Desktop/New folder/Deposco/more_than_100/'+'data'+'_'+str(i)+'.csv')
    if len(df)>max_len:
        max_len=len(df)
print(f'dataset less than 10 data points {count_10}')
print(f'dataset more than 100 data points {count_100}')
print(f'dataset more than 200 data points {count_200}')
print(f'dataset more than 300 data points {count_300}')
print(f'dataset more than 400 data points {count_400}')
print(f'dataset more than 500 data points {count_500}')

len_list.sort()
       

data['timestamp']= pd.to_datetime(data['timestamp']) 
gk = data.groupby('item_id')
gk = data.groupby('timestamp')
test = gk.aggregate(np.sum)
#DataFrame(gk)
type(test) 
test.head()
test.to_csv('C:/Users/Dell/Desktop/New folder/Deposco/'+'data_by_timestamp'+'_'+'.csv')