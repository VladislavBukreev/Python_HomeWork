# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число
# монеток, которые нужно перевернуть, чтобы все монетки были
# повернуты вверх одной и той же стороной. Выведите минимальное
# количество монет, которые нужно перевернуть.

n = int(input("ВВедите количество монет "))
Orel = 0
Reshka = 0
for i in range(1, n + 1):
    x = 0
    x = int(input("Какой стороной вверх лежит эта монета? Нажмите 1 если Орёл, Нажмите 0 если решка. "))
    if x != 0 and x != 1: 
        raise SystemExit("404 вы ввели не то число =(") # Завершение кода
    elif x == 1:
        Orel += 1 
    else:
        Reshka += 1 

if Orel > Reshka:
    Result = n - Orel
else: Result = n - Reshka

print(f"минимальное число монеток, которые нужно перевернуть -> {Result}")

# n = int(input())
# heads_count = 0
# for i in range(n):
#     heads_count += int(input())
# print(min(heads_count, n-heads_count))