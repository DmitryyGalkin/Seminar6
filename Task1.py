"""2) Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123]."""
import random
from timeit import timeit

original_list = []
while len(original_list) < 9:
    new_el = random.randint(1, 30)
    original_list.append(new_el)
print(original_list)
new_list = []
for num, el in enumerate(original_list):
    if original_list[num] > original_list[num - 1]:
        new_list.append(original_list[num])
print(new_list)

print(timeit("new_list", globals=globals(), number=100000))

""" Исользую метод LC, это приводит к сокращению времени обработки 
информации и сокращению строк кода"""

original_list2 = [random.randint(1, 30) for x in range(1, 10)]
print(original_list2)
result_list = [el for num, el in enumerate(original_list2) if
               original_list2[num] > original_list2[num - 1]]
print(result_list)

print(timeit("result_list", globals=globals(), number=100000))

"""3) Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
Необходимо решить задание в одну строку.
Подсказка: использовать функцию range() и генератор."""


my_list = []
el = 20
while el < 241:
    if el % 20 == 0 or el % 21 == 0:
        my_list.append(el)
    el += 1
print(my_list)

# """Использовал LC"""
lc_list = [el for el in range(20, 241) if not el % 20 or not el % 21]
print(lc_list)
print(timeit("my_list", globals=globals(), number=100000))
print(timeit("lc_list", globals=globals(), number=100000))
