import pandas as pd
import seaborn as sns

sales_data = pd.read_csv('datasets/Vendor_Data.csv')
print(sales_data.columns)
print(sales_data.head())
