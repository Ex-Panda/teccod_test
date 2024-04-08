from typing import List


def min_max(a, b) -> List:
    """Принимает на вход два целых числа (минимум и максимум) и возвращает список всех простых чисел в заданном диапазоне."""
    list_numbers = []
    for i in range(a, b + 1):
        list_numbers.append(i)
    return list_numbers


print(min_max(5, 10))
