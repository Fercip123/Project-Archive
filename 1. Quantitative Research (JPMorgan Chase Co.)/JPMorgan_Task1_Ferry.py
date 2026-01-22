import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

class GasPriceModel:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.df['Dates'] = pd.to_datetime(self.df['Dates'])
        self.df = self.df.sort_values('Dates')
        
        self.days_since_start = (self.df['Dates'] - self.df['Dates'].min()).dt.days
        self.prices = self.df['Prices'].values

    def visualize_data(self):
        """Menampilkan grafik tren harga"""
        plt.figure(figsize=(12, 6))
        plt.plot(self.df['Dates'], self.df['Prices'], marker='o', label='Data Historis')
        plt.title('Natural Gas Price Trend Analysis (J.P. Morgan Task 1)')
        plt.xlabel('Years')
        plt.ylabel('Price (USD)')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.show(block=True)

    def get_price_estimate(self, date_str):
        """
        Function to estimate prices on a specific date.
        Supports interpolation (past) and extrapolation (future).
        """
        try:
            target_date = pd.to_datetime(date_str)
            target_day = (target_date - self.df['Dates'].min()).days

            estimated_price = np.interp(target_day, self.days_since_start, self.prices)
            
            return round(estimated_price, 2)
        except Exception as e:
            return f"Error: {e}"

file_csv = r'D:\VScode\Python\TheForage\Quantitative Research (JPMorgan Chase Co.)\Nat_Gas.csv'

try:
    model = GasPriceModel(file_csv)
    
    print("Displaying graph... Close the graph window to proceed to the prediction.")
    model.visualize_data()
    
    print("\n--- PRICE ESTIMATE RESULTS ---")
    
    tgl_past = '2021-05-15'
    print(f"Price estimate on {tgl_past}: ${model.get_price_estimate(tgl_past)}")
    
    tgl_future = '2025-09-30'
    print(f"Price estimate on {tgl_future}: ${model.get_price_estimate(tgl_future)}")

    print("\nThe program is complete. This code is ready to be submitted!")

except FileNotFoundError:
    print("CSV file not found!")