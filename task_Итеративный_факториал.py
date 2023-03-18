def factorial_iterative(n: int) -> int:
    """
    Рассчитать факториал числа n итеративным способом

    :param n: Число, факториал которого нужно найти
    :return: n! - факториал числа n
    """
    factorial = 1
    if n == 0:
        return 1
    if n < 0:
        raise ValueError
    if not isinstance(n, int):
        raise TypeError
    else:
        for num in range(1, n + 1):
            factorial = factorial * num

    return factorial


if __name__ == '__main__':
    print(factorial_iterative(10))
