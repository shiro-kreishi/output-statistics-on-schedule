import json
from typing import Type, TypeVar, List, Union, get_origin, get_args, Dict
from dataclasses import dataclass, asdict, is_dataclass
from .group import Group

# Универсальный шаблонный тип
T = TypeVar('T')


# Универсальная функция загрузки данных из JSON
def load_json(file_path: str, data_type: Union[Type[T], Type[List[T]], Type[Dict[str, T]]]) -> Union[
    T, List[T], Dict[str, T]]:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Если ожидается список объектов
    if get_origin(data_type) is list:
        item_type = get_args(data_type)[0]
        if isinstance(data, list):
            return [item_type(**item) if is_dataclass(item_type) else item for item in data]
        else:
            raise TypeError("Ожидался массив объектов JSON")

    # Если ожидается словарь объектов
    elif get_origin(data_type) is dict:
        key_type, value_type = get_args(data_type)
        if isinstance(data, dict) and key_type is str:
            return {key: value_type(**value) if is_dataclass(value_type) else value for key, value in data.items()}
        else:
            raise TypeError("Ожидался словарь объектов JSON с ключами-строками")

    # Если ожидается один объект
    elif is_dataclass(data_type):
        if isinstance(data, dict):
            return data_type(**data)
        else:
            raise TypeError("Ожидался одиночный объект JSON")

    # Если не подходит под ожидаемый тип
    raise TypeError("Тип данных не соответствует JSON-структуре")