# Importing necessary libraries
import yfinance as yf
import pandas as pd

# Downloading historical forex data
symbol = "EURUSD=X"
start_date = "2000-01-01"
end_date = "2023-11-30"
interval = '15m'
data = yf.download(symbol, start=start_date, end=end_date, interval=interval)

# Displaying the last row of the data
last_row = data.iloc[-1:, :]

# Displaying the 'Open' column of the last row
last_open_price = last_row['Open'].values[0]

# Printing the result
print(f"Last Open Price: {last_open_price}")