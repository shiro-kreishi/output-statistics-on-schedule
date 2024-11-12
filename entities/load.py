import json
from typing import Type, TypeVar, List, Union, get_origin, get_args
from dataclasses import dataclass, asdict, is_dataclass

# Универсальный шаблонный тип
T = TypeVar('T')


# Универсальная функция загрузки данных из JSON
def load_json(file_path: str, data_type: Union[Type[T], Type[List[T]]]) -> Union[T, List[T]]:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Проверяем, ожидается ли список объектов
    if get_origin(data_type) is list:
        item_type = get_args(data_type)[0]
        if isinstance(data, list):
            return [item_type(**item) if is_dataclass(item_type) else item for item in data]
        else:
            raise TypeError("Ожидался массив объектов JSON")

    # Проверяем, ожидается ли одиночный объект
    elif is_dataclass(data_type):
        if isinstance(data, dict):
            return data_type(**data)
        else:
            raise TypeError("Ожидался одиночный объект JSON")

    # Если не подходит под ожидаемый тип
    raise TypeError("Тип данных не соответствует JSON-структуре")