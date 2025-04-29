import yfinance as yf
import pandas as pd

# Define ticker (for example: S&P 500 index '^GSPC' or AAPL for Apple)
ticker = 'AAPL'

# Date range
start_date = '2019-01-01'
end_date = '2023-12-31'

# Download stock data
data = yf.download(ticker, start=start_date, end=end_date, progress=False)

# Reset index to get 'Date' as a column
data = data.reset_index()

# Save directly to CSV
data.to_csv('stock_data.csv', index=False)

print("✅ Saved stock_data.csv correctly!")
