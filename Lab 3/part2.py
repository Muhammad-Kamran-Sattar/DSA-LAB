# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 14:09:44 2025

@author: mkamr
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "dailyActivity_merged.csv"
df = pd.read_csv(file_path)

# Convert ActivityDate to datetime
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])
date_filter = "2016-04-12"
day_data = df[df['ActivityDate'] == date_filter]

if not day_data.empty:
    values = [
        day_data['VeryActiveDistance'].sum(),
        day_data['ModeratelyActiveDistance'].sum(),
        day_data['LightActiveDistance'].sum(),
        day_data['SedentaryActiveDistance'].sum()
    ]
    labels = ["Very Active", "Moderately Active", "Light Active", "Sedentary"]

    plt.figure(figsize=(8,8))
    plt.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
    plt.title("Activity Distance Breakdown on 12th April 2016", fontsize=14)
    plt.show()
else:
    print("No data available for 12th April 2016 in the dataset.")