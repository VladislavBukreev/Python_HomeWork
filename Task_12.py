# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя –
# школьница. Петя помогает Кате по математике. Он задумывает два
# натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для
# этого Петя делает две подсказки. Он называет сумму этих чисел S и их
# произведение P. Помогите Кате отгадать задуманные Петей числа.

# Решение через квадратное уравнение
# X + Y = S (Сумма)
# X * Y = P (Произведение)
# x = x * s - x^2 - p = 0
# y = x^2 - s*x + p
# d(дискриминант) = b^2 - 4ac




s = int(input("Какая сумма чисел ? :"))
p = int(input("Какое произведение чисел?  :"))


d =  s**2 - 4*1*p
x1 = (s + (d ** (0.5))) / 2

y = (s - (d ** (0.5))) / 2

print(f"Число 1 - {x1} Число 2 - {y}")