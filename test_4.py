from typing import List, Tuple


def len_str(list_line: List) -> Tuple[List, List]:
    """Сортирует список строк по длине, сначала по возрастанию, а затем по убыванию"""
    return sorted(list_line, key=len), sorted(list_line, key=len, reverse=True)


print(len_str(["Привет", "Солнце", "Кот", "Дом", "Яблоко", "Автомобиль", "Телефон", "Университет"]))
