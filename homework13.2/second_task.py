import logging
import json
from json import JSONDecodeError
from pathlib import Path

logging_json_file = logging.getLogger("JsonLogger")
logging_json_file.setLevel(logging.ERROR)
handler = logging.FileHandler("json_validation.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logging_json_file.addHandler(handler)

path = "/homework13.2/json_files"
def is_json_file_is_valid(folder_path):

    for file in Path(folder_path).glob("*.json"):
            try:
                with open(file, "r", encoding="utf-8") as json_file:
                    json.load(json_file)
                print(f"file is valid {file.name}")
            except JSONDecodeError:
                logging_json_file.error(f"Json file {file} is invalid")


is_json_file_is_valid(path)