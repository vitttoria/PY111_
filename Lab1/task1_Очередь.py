"""
My little Queue
"""
from typing import Any


class Queue:
    def __init__(self):
        """
        Очередь с помощью python list
        Начало - первый добавленный элемент в списке под индексом 0
        Конец - последний добавленный элемент в список
        """
        self.queue = list()

    def enqueue(self, elem: Any) -> None:
        """
        Добавление элемент в конец очереди

        :param elem: Элемент, который должен быть добавлен
        """
        self.queue.append(elem)

    def dequeue(self) -> Any:
        """
        Извлечение элемента из начала очереди.

        :raise: IndexError - Ошибка, если очередь пуста

        :return: Извлеченный с начала очереди элемент.
        """
        if not self.queue:
            raise IndexError

        return self.queue.pop(0)

    def peek(self, ind: int = 0) -> Any:
        """
        Просмотр произвольного элемента, находящегося в очереди, без его извлечения.

        :param ind: индекс элемента (отсчет с начала, 0 - первый с начала элемент в очереди, 1 - второй с начала
        элемент в очереди, и т.д.)

        :raise: TypeError - если указан не целочисленный тип индекса
        :raise: IndexError - если индекс вне границ очереди

        :return: Значение просмотренного элемента
        """
        if not isinstance(ind, int):
            raise TypeError

        if not 0 <= ind <= len(self.queue):
            raise IndexError

        return self.queue[ind]

    def clear(self) -> None:
        """ Очистка очереди. """
        self.queue = list()

    def __len__(self):
        """ Количество элементов в очереди. """
        return len(self.queue)


if "__main__" == __name__:
    q = Queue()
    q.enqueue(5)
    print("Добавили 5 в очередь")
    print(q.queue)
    print(q.peek(0))
    print("Просматриваем нулевой элемент")
    q.enqueue(9)
    print("Добавили 9 в очередь")
    print(q.queue)
    print(q.peek(1))
    print("Просматриваем первый элемент")
    q.enqueue(4)
    print(q.queue)
    print("Добавили 4 в очередь")
    print(q.peek(2))
    print("Просматриваем второй элемент")
    print(q.dequeue())
    print("Извлекаем элемент из начала очереди")
    print(q.queue)
    print(q.__len__())
    print("Длина списка")
    q.clear()
    print("Очистили список")
    print(q.queue)
