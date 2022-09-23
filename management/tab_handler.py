from cgi import test
from utils.json_handler import read_json
from datetime import datetime

FORMATED_DATE_STR = "%d/%m/%Y %H:%M:%S"


def date_debit_close():
    today = datetime.now()
    return today.strftime(FORMATED_DATE_STR)


def calculate_tab(table_consumption: list) -> dict:
    products = read_json("./menu.json")

    bill_values = []

    for product in products:
        for total in table_consumption:
            if product['id'] == total['id']:
                bill_values.append(total['amount'] * product['price'])

    return {'subtotal': sum(bill_values), 'created_at': date_debit_close()}
