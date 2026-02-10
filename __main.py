import pandas as pd
import config
from utils import first_name
from data_processing import process_invoices, process_merge

# Get the first day of the current month
today = pd.Timestamp.now().date()
first_day_this_month = today.replace(day=1)

# Create two databases, one for the customer and another for the invoice information
df = pd.read_csv(config.CUSTOMER_URL)
df2 = pd.read_csv(config.INVOICE_URL)

# Create 2 new databasas. One for the pending invoices of previous months, and another for the invoices of the current month
df2['Date'] = pd.to_datetime(df2['Date']).dt.date
df2.loc[:, ['Amount', 'Open Balance']] = df2[['Amount', 'Open Balance']].apply(pd.to_numeric, errors='coerce')
df_pending_invoices = df2.loc[df2['Date']<first_day_this_month].copy()
df_current_invoices = df2.loc[df2['Date']>=first_day_this_month].copy()

df_pending_summary = process_invoices(df_pending_invoices)
df_current_summary = process_invoices(df_current_invoices)

# Filter the relevant columns on df, and then change the data type of Price, to be able to filter.
df_customers = df[['Name','Open Balance', 'Type']].copy()
df_customers['Open Balance'] = pd.to_numeric(df_customers['Open Balance'],errors='coerce')
df_customers['First Name'] = df_customers.apply(first_name, axis=1)

df_merged = process_merge(df_customers, df_pending_summary, df_current_summary)

print(df_merged)