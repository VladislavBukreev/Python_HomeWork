# Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
# . Последняя строка содержит число X
import random

n = int(input('Введите размер массива : '))

a = []
a.append(random.randint(1,n))
for i in range(1,n):
    a.append(random.randint(1,20))
print(a)
x = int(input('Какое число ищем? : '))

count = 0
for i in range(1,n):
    if a[i] == x:
        count += 1
print(f" Число X повторялось {count} раз")