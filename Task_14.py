# Задача 14: Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.

n=int(input("Задайте число"))
x=1
while x<=n:
    print(x)
    x=x*2
