# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 14:09:40 2025

@author: mkamr
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "dailyActivity_merged.csv"
df = pd.read_csv(file_path)

# Convert ActivityDate to datetime
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])
plt.figure(figsize=(10,6))
plt.scatter(df['ActivityDate'], df['SedentaryMinutes'], color='green')
plt.title("Sedentary Minutes (Daily)", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Sedentary Minutes", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.6)
plt.tight_layout()
plt.show()
