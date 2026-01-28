# I'll create the string that I print in the client emails, following this format example:
# "#11111, 01/01/2026, $100 - Invoice link"

def invoice_details(row):
    num = row['Num']
    date = row['Date']
    amount = row['Open Balance']

    return f"#{num}, {date}, ${amount} - Invoice Link"