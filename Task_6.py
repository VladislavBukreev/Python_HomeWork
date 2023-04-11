# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

a = int(input("Введите ваш номер билета :"))

if len(str(a)) == 6:
    b = a//1000  # Выявляем первую половину

    one = b // 100
    two = b // 10 % 10    
    three = b % 10

    c = a % 1000 # Выявляем вторую половину

    four = c // 100
    five = c // 10 % 10
    six = c % 10

    if (one+two+three)==(four+five+six):
        print ('Ваш билетик Счастливый!')
    else:
        print ('Ваш билетик Обычный =(')
else:
    print("Это не номер билета!")