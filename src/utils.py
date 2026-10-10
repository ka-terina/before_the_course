import json
import os


def read_json(path: str) -> dict:
    """ """
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
