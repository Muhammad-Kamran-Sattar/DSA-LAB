# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 14:09:29 2025

@author: mkamr
"""

import pandas as pd
import matplotlib.pyplot as plt
daily_path = "dailyActivity_merged.csv"   # Daily activity
sleep_path = "sleepDay_merged.csv"        # Sleep data
hourly_path = "hourlySteps_merged.csv"    # Hourly steps data

df_daily = pd.read_csv(daily_path)
df_sleep = pd.read_csv(sleep_path)
df_hourly = pd.read_csv(hourly_path)

# Convert dates to datetime
df_daily['ActivityDate'] = pd.to_datetime(df_daily['ActivityDate'])
df_sleep['SleepDay'] = pd.to_datetime(df_sleep['SleepDay'])
df_hourly['ActivityHour'] = pd.to_datetime(df_hourly['ActivityHour'])