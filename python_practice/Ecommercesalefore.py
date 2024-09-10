import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA


df = pd.read_csv('sales_data.csv')


df['Date'] = pd.to_datetime(df['Date'])# Convert 'Date' column to datetime format

# Plot the time series
plt.figure(figsize=(10, 6))
plt.plot(df['Date'], df['Sales'], marker='d')
plt.xlabel('Date')
plt.ylabel('Sales')
plt.title('Daily Sales Data')
plt.grid(True)
plt.show()


model = ARIMA(df['Sales'], order=(1, 1, 1))  # Example ARIMA model# Train ARIMA model
fit_model = model.fit()

# Forecast future sales (e.g., next 7 days)
forecast = fit_model.forecast(steps=10)# Forecast future sales (e.g., next 7 days)


print("Forecasted Sales:")
print(forecast)
