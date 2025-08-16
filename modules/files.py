import csv
import os
import json

import requests


def read_csv_file(file_path: str) -> list:
    with open(file_path, encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)


def add_csv_line(file_path: str, line: str) -> None:
    with open(file_path, 'a', encoding="utf-8", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(line)


def save_json_file(file_content: str, 
                   file_path:str, 
                   ensure: bool = True
                   ) -> None:
    slash = '/'
    if not file_path.endswith(slash) and not file_path.endswith('.json'):
        file_path = file_path + slash
    with open(file_path, 'w', encoding="utf-8") as new_j_file:
        json.dump(file_content, new_j_file, indent=4, ensure_ascii=ensure)


def read_json_file(file_path: str) -> dict:
    with open(file_path, 'r', encoding="utf-8") as json_file:
        return json.load(json_file)
    

def update_json_file(file_path: str, key: str, 
                     value: str | int | bool | list
                     ) -> None:
    data = read_json_file(file_path)
    data[key] = value
    save_json_file(data, file_path)


def dowload_file_from_url(url:  str, save_path: str) -> None:
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)


def check_file_exists(file_path: str) -> bool:
    return os.path.exists(file_path)


def create_env_file(path: str, content: str) -> None:
    with open(path, 'w') as env_file:
        env_file.write(content)


def delete_file(path: str) -> None:
    os.remove(path)


def write_file(path: str, content: str, method: str = 'w') -> None:
    with open(path, method) as file:
        file.write(content)


def create_folder(path, ingnor_FileExistsError=False):
    try:
        os.mkdir(path)
    except FileExistsError as error:
        if not ingnor_FileExistsError:
            raise