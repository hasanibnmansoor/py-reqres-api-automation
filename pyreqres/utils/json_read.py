import json
from collections import namedtuple

__all__ = ["parse_json_file"]


def parse_json_file(json_file_path: str):
    with open(json_file_path, "r") as jf:
        data = json.load(jf)
    Data = namedtuple("Data", data)
    return Data(**data)
