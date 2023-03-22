from typing import List


def car_paths(n: int, m: int) -> List[List[int]]:
    """
    Просчитать количество маршрутов до каждой клетки с учетом возможных перемещений.

    :param n: Количество строк в таблице
    :param m: Количество столбцов в таблице

    :return: Новую таблицу с посчитанным количеством маршрутов в каждую клетку
    """

    if n == 1 and m == 1:
        return [[1]]

    paths = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            paths[i][j] = paths[i - 1][j] + paths[i][j - 1] + paths[i - 1][j - 1]
            print(paths)
    return paths


if __name__ == '__main__':
    paths = car_paths(4, 4)
    print(paths[-1][-1])  # 7
