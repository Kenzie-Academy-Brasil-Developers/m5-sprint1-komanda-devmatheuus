from utils.json_handler import read_json, write_json
from management.tab_handler import calculate_tab

DATA_BASE_PATCH = "./menu.json"

if __name__ == "__main__":
    # print(read_json(DATA_BASE_PATCH))

    # new_item = {"name": "CHURROS DO M5", "price": 5.0}
    # print(write_json(DATA_BASE_PATCH, new_item))

    table_1 = [{'id': 1, 'amount': 5}, {'id': 19, 'amount': 5}]
    print(calculate_tab(table_1))
