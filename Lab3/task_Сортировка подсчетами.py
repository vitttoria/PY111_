from typing import Sequence


def sort(container: Sequence[int]) -> Sequence[int]:
    """
    Сортировка подсчетами

    1. Определите максимальное значение в массиве и заполните вспомогательный массив с подсчетом количества элементов.
    2. Посчитайте количество каждого объекта
    3. Зная количество каждого объекта, восстановите отсортированный массив

    :param container: Массив, который надо отсортировать
    :return: Отсортированный в порядке возрастания массив
    """
    if not container:
        return []
    if len(container) == 1:
        return container

    container_ = [0] * len(container)

    for i in range(len(container)):  # длина-11 (0,1,2,3,4,5,6,7,8,9,10)
        container_[container[i]] += 1  # ведем счетчик значений в массиве container_
    # return container_

    sorted_container = []
    for key, value in enumerate(container_):
        sorted_container.append([key] * value)
    return sum(sorted_container, [])


if __name__ == '__main__':
    # print(sort([10, 6, 1, 1, 2, 6, 5, 10, 2, 3, 10]))
    print(sort([1]))
