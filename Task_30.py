# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def create_list_progression(a1,d,n): 
    return [a1 + i * d for i in range(n)]

a1 = int(input("Bведитe первый элемент арифм, посл-ти: "))
n = int(input("Введите кол-во элементов арифм. посл-ти: "))
d = int(input("Введите шаг арифм. посл-ти: "))

print(" Последовательность: ")
print(*create_list_progression(a1,d,n))