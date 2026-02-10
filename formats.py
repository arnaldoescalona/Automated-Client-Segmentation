import textwrap
import pandas as pd


def skipped_month(row):
    #Name	Open Balance	Type	First Name	Customer	Invoice Details_x	Invoice Count_x	Invoice Details_y	Invoice Count_y
    name = row['First Name']
    pending_invoice = row['Invoice Details_x']
    current_invoice = row['Invoice Details_y']

    string = textwrap.dedent(f'''\
                Payment Reminder for Missing Month
                
                Hello {name},
                
                I hope this email finds you well. Just a reminder that we have not received a payment for the following invoice yet, this month of service was skipped with payment. We kindly request that you settle the outstanding amount promptly.
                
                If you have already made the payment and can provide a receipt, please disregard this message. Otherwise, please make the payment at your earliest convenience. You can find the payment details below:
                
                {pending_invoice}''')
                
                
    if pd.notna(current_invoice):
        string += textwrap.dedent(f'''\
                                 
                                  
                Additionally, this month's invoice, which is due by the last day of the month:
                
                {current_invoice}''')
        
    string += textwrap.dedent(f'''\
                
                              
        Thank you for your attention to this matter. If you have any questions or need further assistance, feel free to reach back to us.
                
        Best regards,''')
    return string