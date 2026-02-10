import pandas as pd
from utils import first_name, invoice_details

def process_invoices(df):
    # I create a summary df from the invoice df, with the invoice details and the count of how many invoices each client has.
    df['Date'] = df['Date'].dt.strftime('%m/%d/%Y')

    df['Invoice Details'] = df.apply(invoice_details, axis=1)
    df_aux1 = df.groupby("Customer")['Invoice Details'].agg('\n '.join).reset_index()

    df_aux2= df.groupby("Customer")[["Open Balance"]].count().reset_index()
    df_aux2 = df_aux2.rename(columns={"Open Balance": "Invoice Count"})

    df_summary = df_aux1.merge(df_aux2)
    return df_summary

def process_merge(df1, df2, df3):
    df_merged = df1.merge(df2, left_on='Name', right_on='Customer')
    df_merged = df_merged.merge(df3, how='left', on='Customer')
    df_merged = df_merged.drop('Customer', axis=1)

    return df_merged
