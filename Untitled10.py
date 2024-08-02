#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install yfinance


# In[2]:


import yfinance as yf


# In[3]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


# In[4]:


# Define the ticker symbol and the time period
ticker = "BAC"
start_date = "2020-01-01"
end_date = "2024-07-31"

# Fetch the data
data = yf.download(ticker, start=start_date, end=end_date, progress=False)


# In[5]:


# Display the first few rows of the data
print(data.head())

# Check for missing values
print(data.isnull().sum())

# If there are missing values, handle them (e.g., by interpolation or dropping)
data = data.interpolate()


# In[6]:


# Extract adjusted close prices
adj_close = data['Adj Close']


# In[7]:


# Plotting the adjusted closing prices
plt.figure(figsize=(14, 7))
plt.plot(adj_close, label='Adjusted Close Price')
plt.title('Bank of America Adjusted Closing Prices (Jan 2020 - July 2024)')
plt.xlabel('Date')
plt.ylabel('Adjusted Close Price')
plt.legend()
plt.grid(True)
plt.show()


# In[8]:


# Descriptive statistics
print(adj_close.describe())

# Calculate daily returns
daily_returns = adj_close.pct_change()

# Plot daily returns
plt.figure(figsize=(14, 7))
plt.plot(daily_returns, label='Daily Returns')
plt.title('Bank of America Daily Returns (Jan 2020 - July 2024)')
plt.xlabel('Date')
plt.ylabel('Daily Returns')
plt.legend()
plt.grid(True)
plt.show()

# Histogram of daily returns
plt.figure(figsize=(10, 6))
sns.histplot(daily_returns.dropna(), bins=50, kde=True)
plt.title('Distribution of Daily Returns')
plt.xlabel('Daily Returns')
plt.ylabel('Frequency')
plt.show()


# In[9]:


# Calculate moving averages
data['30-Day SMA'] = adj_close.rolling(window=30).mean()
data['90-Day SMA'] = adj_close.rolling(window=90).mean()

# Plotting moving averages
plt.figure(figsize=(14, 7))
plt.plot(adj_close, label='Adjusted Close')
plt.plot(data['30-Day SMA'], label='30-Day SMA')
plt.plot(data['90-Day SMA'], label='90-Day SMA')
plt.title('Adjusted Close Price with Moving Averages')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.grid(True)
plt.show()


# In[ ]:


# Example: ARIMA model (not detailed here)
from statsmodels.tsa.arima_model import ARIMA

model = ARIMA(adj_close, order=(5, 1, 0))
model_fit = model.fit(disp=0)
print(model_fit.summary())

# # Plotting forecast
model_fit.plot_predict(start='2023-01-01', end='2024-12-31')
plt.show()


# In[16]:


def analyze_stock(ticker, start_date, end_date):
    # Fetch data, analyze, and visualize (reuse the steps above)
    pass

# Example usage:
analyze_stock("AAPL", "2020-01-01", "2024-07-31")

