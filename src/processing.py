def filter_by_state(list_of_dicts: list, state: str = "EXECUTED") -> list:
    """Функция, которая фильтрующая данные из списка словарей по признаку состояния 'EXECUTED/CANCELED'"""

    filtered_dicts = []
    for income_dict in list_of_dicts:
        if income_dict["state"] == state:  # Производится выборка из полученнных данных по заданному параметру
            filtered_dicts.append(income_dict)  # и и заливка этой выборки в новый список словарей
    return filtered_dicts


def sort_by_date(list_of_dicts: list, sort_order_descending: bool = True) -> list:
    """Функция, которая делает сортировку в списке словарей по дате"""

    sorted_dicts = sorted(list_of_dicts, key=lambda income_dict: income_dict["date"], reverse=sort_order_descending)
    return sorted_dicts  # Для сортировки используется вcтроенная lambda-функция с записью в новый список словарей
