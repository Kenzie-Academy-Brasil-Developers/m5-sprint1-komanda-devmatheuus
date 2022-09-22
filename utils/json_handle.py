import json

def next_id(database_patch: str) -> int:
    products = read_json(database_patch)

    if len(products) == 0:
        return 1

    return products[-1]['id'] + 1

def read_json(database_patch: str) -> list:
    try:
        with open(database_patch, "r", encoding="utf8") as database:
            database_data = json.load(database)
            return database_data

    except FileNotFoundError or len(database_data) == 0:
        return []


def write_json(database_patch: str, item: dict) -> None:

    database_data = read_json(database_patch)

    item.update({"id": next_id(database_patch)})
    
    organized_item = {
      "id": item["id"],
      "name": item["name"],
      "price": item["price"]
    }

    database_data.append(organized_item)

    with open(database_patch, "w") as file:
        json.dump(database_data, file, indent=4)
