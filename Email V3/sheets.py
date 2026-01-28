import pandas as pd

# Gaining access to the copy of the file. It's just the copy to be able to edit it while doing my job.
customer_sheet = '1r3KvHllGkuvUhu-Z_gMQ3gQVVAeWkTZBkdFRW_aB_M4'
invoices_gid = '1234385958'

# Get the first day of the current month
today = pd.Timestamp.now().date()
first_day_this_month = today.replace(day=1)

# Create two databases
# df: Client Database
# df2: Invoice Database
df = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{customer_sheet}/export?format=csv')
df2 = pd.read_csv(f'https://docs.google.com/spreadsheets/d/{customer_sheet}/export?format=csv&gid={invoices_gid}')

# Filter the relevant columns on df, and then change the data type of Price, to be able to filter.
df_customers = df[['Name','Payment Method', 'Phone Number', 'Email', 'Price', 'Type', 'Last']]
df_customers.loc[:, 'Price'] = pd.to_numeric(df_customers['Price'],errors='coerce')
df_customers[df_customers['Price']>0]

# Create 2 new databasas. One for the pending invoices of previous months, and another for the invoices of the current month
df2['Date'] = pd.to_datetime(df2['Date']).dt.date
df2.loc[:, ['Amount', 'Open Balance']] = df2[['Amount', 'Open Balance']].apply(pd.to_numeric, errors='coerce')
df_pending_invoices = df2.loc[df2['Date']<first_day_this_month].copy()
df_current_invoices = df2.loc[df2['Date']>=first_day_this_month].copy()