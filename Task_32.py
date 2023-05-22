# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
def find_idxs_in_bounds(lst, lower_bound, upper_bound):
    return [idx for idx, elem in enumerate(lst) if lower_bound <= elem <= upper_bound]

n = int(input("Введите кол-во символов для генерации списка : "))
lower_bound = int(input("Введите нижнюю границу значений для нахождения индекса "))
upper_bound = int(input("Введите верхнюю границу значений для нахождения индекса "))
lst_random = [random.randint(-100 , 100) for _ in range(n)]

print(f"Случайный список : {lst_random}")
print(f"Индексы значений в диапазоне : [{lower_bound}; {upper_bound}]")
print(find_idxs_in_bounds(lst_random, lower_bound, upper_bound))