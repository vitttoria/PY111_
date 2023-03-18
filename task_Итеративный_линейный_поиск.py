"""
This module implements some functions based on linear search algo
"""
from typing import List


def min_search(arr: List[int]) -> int:
    """
    Функция для поиска минимума в массиве

    :param arr: Массив целых чисел
    :return: Индекс первого вхождения элемента в массиве
    """
    if not arr:
        raise ValueError
    ind_min = 0
    min_element = arr[ind_min]
    index = 1

    for _ in arr:
        if len(arr) > index and arr[index] < min_element:
            min_element = arr[index]
            ind_min = index
        index = index + 1
        # if len(arr) == 1:
        #     return 0
    return ind_min

    # if not arr:
    #     raise ValueError
    # ind_min = 0
    # min_val = arr[ind_min]
    # ind = 1
    # for num in arr:
    #     if ind < len(arr) and arr[ind] < min_val:
    #         min_val = arr[ind]
    #         ind_min = ind
    #     ind = ind + 1
    # return ind_min


if __name__ == '__main__':
    print(min_search([-200]))
