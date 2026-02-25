def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """Функция, которая фильтрующая данные из списка словарей по признаку состояния 'EXECUTED/CANCELED'"""

    filtered_dicts = []
    for dict in list_of_dicts:
        if dict["state"] == state:  # Производится выборка из полученнных данных по заданному параметру
            filtered_dicts.append(dict)  # и и заливка этой выборки в новый список словарей
    return filtered_dicts
