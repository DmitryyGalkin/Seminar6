"""2) Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]."""
import random
from memory_profiler import profile


@profile
def create_list():
    my_list = []
    el = 20
    while el < 242:
        my_list.append(el)
        el += 1
    print(my_list)

    result_list = []
    for el in my_list:
        if el % 20 == 0 or el % 21 == 0:
            result_list.append(el)
        el += 1

    print(result_list)

create_list()

"""Вместо массива исходного массива, сразу  сгенерировал конечный массив"""
@profile()
def create_list2():
  lc_list = [el for el in range(20, 241) if not el % 20 or not el % 21]
  print(lc_list)
  del lc_list
create_list2()
