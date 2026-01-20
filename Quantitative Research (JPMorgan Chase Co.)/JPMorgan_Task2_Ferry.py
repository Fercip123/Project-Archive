import pandas as pd
import numpy as np
from sympy import interpolate

def get_contract_value(injection_date, withdrawal_date, volume, injection_withdrawal_cost, storage_cost_per_month):
    """
    Calculates the estimated net value of a gas storage contract.
    
    Parameters:
    - injection_date (str): Date when gas is purchased and stored (e.g., '2022-06-01').
    - withdrawal_date (str): Date when gas is withdrawn and sold (e.g., '2022-12-01').
    - volume (float): Total volume of gas in MMBtu.
    - injection_withdrawal_cost (float): Fee per unit for injecting/withdrawing gas.
    - storage_cost_per_month (float): Fixed monthly rental fee for the storage facility.
    """
    
    # 1. Fetch estimated prices using the model from Task 1
    # Note: Ensure your 'interpolate' function from Task 1 is defined in your script
    price_at_injection = interpolate(injection_date)
    price_at_withdrawal = interpolate(withdrawal_date)
    
    # 2. Calculate Transactional Costs (Operational costs)
    # Applied when injecting and withdrawing gas
    total_trans_cost = volume * injection_withdrawal_cost
    
    # 3. Calculate Time-based Storage Costs
    start_dt = pd.to_datetime(injection_date)
    end_dt = pd.to_datetime(withdrawal_date)
    
    # Calculate difference in months
    duration_months = (end_dt.year - start_dt.year) * 12 + (end_dt.month - start_dt.month)
    total_storage_cost = duration_months * storage_cost_per_month
    
    # 4. Final Financial Calculation
    # Total Outflow: Cost of buying gas + operational fees + storage rent
    total_expenditure = (volume * price_at_injection) + total_trans_cost + total_storage_cost
    
    # Total Inflow: Revenue from selling gas
    total_revenue = volume * price_at_withdrawal
    
    # Net Contract Value (Profit or Loss)
    net_value = total_revenue - total_expenditure

# Define model parameters
amplitude = 10.0
shift = 0.0
slope = 0.05
intercept = 50.0
start_date = '2022-01-01'

def interpolate(date_to_predict):
    days = (pd.Timestamp(date_to_predict) - pd.Timestamp(start_date)).days
    
    return amplitude * np.sin(days * 2 * np.pi / 365 + shift) + days * slope + intercept

def get_contract_value(injection_date, withdrawal_date, volume, injection_withdrawal_cost, storage_cost_per_month):
    price_at_injection = interpolate(injection_date)
    price_at_withdrawal = interpolate(withdrawal_date)
    
    total_trans_cost = volume * injection_withdrawal_cost
    
    start_dt = pd.to_datetime(injection_date)
    end_dt = pd.to_datetime(withdrawal_date)
    duration_months = (end_dt.year - start_dt.year) * 12 + (end_dt.month - start_dt.month)
    total_storage_cost = duration_months * storage_cost_per_month
    
    total_expenditure = (volume * price_at_injection) + total_trans_cost + total_storage_cost
    total_revenue = volume * price_at_withdrawal
    
    return total_revenue - total_expenditure

# --- Example Execution ---
# Scenario: Storing 100,000 units from Summer to Winter
test_volume = 100000 
test_inj_cost = 0.01   # $0.01 per unit
test_storage_fee = 5000 # $5,000 fixed monthly fee

contract_profit = get_contract_value('2022-06-01', '2022-12-01', test_volume, test_inj_cost, test_storage_fee)

print(f"Projected Contract Value: ${contract_profit:,.2f}")