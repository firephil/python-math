import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf

  # Get the data of the stock
msft = yf.Ticker('MSFT')

  # Get the historical market data
hist = msft.history(period='3mo')

  # Plot the closing prices
plt.figure(figsize=(10,6))
plt.plot(hist.index, hist['Close'])
plt.title('Microsoft Stock Price (Last 3 Months)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.grid(True)
plt.show()