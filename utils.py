# Receives the name of the customer in the format: "Last_name, First_name", and returns only First_name.
# There are some customers (commercial buildings) whose name are "Company_name". In that case, return Company_name

import pandas as pd

def first_name(row):
    name = row["Name"]
    if len(name.split(', ')) > 1:
        return name.split(', ')[1]
    else:
        return name.split(', ')[0]



# I'll create the string that I print in the client emails, following this format example:
# "#11111, 01/01/2026, $100 - Invoice link"

def invoice_details(row):
    if pd.isna(row['Num']):
        return ""
    else:
        num = int(row['Num'])
        date = row['Date']
        amount = row['Open Balance']
        return f"\u2022 #{num}, {date}, ${amount} - Invoice Link"