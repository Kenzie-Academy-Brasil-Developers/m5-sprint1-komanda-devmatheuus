from datetime import datetime, timedelta

FORMATED_DATE_STR = "%d/%m/%Y %H:%M:%S"


def date_debit_close():
    today = datetime.now()
    return today.strftime(FORMATED_DATE_STR)


def calculate_tab(table_consumption: list) -> dict:
    bill_values = []

    for total in table_consumption:
        bill_values.append(total['amount'])

    return {'subtotal': sum(bill_values), 'created_at': date_debit_close()}
