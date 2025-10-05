# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 14:00:19 2025

@author: mkamr
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = "dailyActivity_merged.csv"   # <-- change path if file is in another folder
df = pd.read_csv(file_path)

# Convert ActivityDate to datetime
df['ActivityDate'] = pd.to_datetime(df['ActivityDate'])

# Group by date and sum steps (if multiple users exist per day)
daily_steps = df.groupby('ActivityDate')['TotalSteps'].sum()

# Plot line chart
plt.figure(figsize=(12,6))
plt.plot(daily_steps.index, daily_steps.values, marker='o', linestyle='-', color='b')
plt.title("Total Number of Steps on Daily Basis", fontsize=14)
plt.xlabel("Date", fontsize=12)
plt.ylabel("Total Steps", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()