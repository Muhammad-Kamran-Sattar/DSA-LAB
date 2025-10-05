# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 15:28:57 2025

@author: mkamr
"""

import matplotlib.pyplot as plt  
import pandas as pd 
df = pd.read_csv('population_by_country_2020.csv' )  
print(df.dtypes) 
list1 = df['Country (or dependency)'].values.tolist()  
list2 = df['Population (2020)'].values.tolist()  
plt.bar(list1, list2,width = 1, color = ['red', 'green']) 
plt.show() 