from utils.json_handle import read_json, write_json

DATA_BASE_PATCH = "./menu.json"

if __name__ == "__main__":
    print(read_json(DATA_BASE_PATCH))

    # new_item = {"name": "CHURROS DO M5", "price": 5.0}
    # print(write_json(DATA_BASE_PATCH, new_item))
