import pandas as pd
import numpy as np

# Step 1: Load your stock data
stock_df = pd.read_csv('stock_data.csv')  # your input

# Step 2: Use 'Close' column instead of 'Adj Close'
stock_df['Log_Returns'] = np.log(stock_df['Close'] / stock_df['Close'].shift(1))

# Step 3: Drop first row (NaN log return)
stock_df = stock_df.dropna().reset_index(drop=True)

# Step 4: Create Index column
stock_df['Index'] = np.arange(len(stock_df))

# Step 5: Create normalized data
mean_lret = stock_df['Log_Returns'].mean()
sd_lret = stock_df['Log_Returns'].std()
stock_df['Data'] = (stock_df['Log_Returns'] - mean_lret) / sd_lret

# Step 6: Save normalized data CSV
normalized_df = stock_df[['Index', 'Date', 'Data']]
normalized_df.to_csv('AAPL_normalized_data.csv', index=False)
print("✅ Saved normalized_data.csv")

# Step 7: Save parameters CSV
delta = 0.20468  # manually given
mean_InvLam = 0.0153569567470876
sd_InvLam = 0.698872008410086

param_df = pd.DataFrame([{
    'delta': delta,
    'mean_lret': mean_lret,
    'sd_lret': sd_lret,
    'mean_InvLam': mean_InvLam,
    'sd_InvLam': sd_InvLam
}])

param_df.to_csv('AAPL_parameters.csv', index=False)
print("✅ Saved parameters.csv")
