# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 14:09:10 2025

@author: mkamr
"""
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "dailyActivity_merged.csv"
df = pd.read_csv(file_path)

# Convert ActivityDate to datetime
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])    # Hourly steps data

daily_distance = df.groupby('ActivityDate')['TotalDistance'].sum()

plt.figure(figsize=(12,6))
plt.bar(daily_distance.index, daily_distance.values, color='orange')
plt.title("Daily Distance Covered", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total Distance (miles)", fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()