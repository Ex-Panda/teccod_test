from typing import List


def unic_list(num_list) -> List:
    """Принимает на вход список целых чисел и возвращает новый список, содержащий только уникальные элементы из исходного списка."""
    return list(set(num_list))


a = [1, 2, 3, 4, 5, 1, 2, 5, 3, 8, 8, 9]

print(unic_list(a))
