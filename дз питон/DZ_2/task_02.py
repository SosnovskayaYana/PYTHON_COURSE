#  Задача №2:
#  петя задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
#   Петя делает две подсказки. сумма этих чисел S и их произведение P. 
#   Помогите Кате отгадать задуманные Петей числа.
#  Пример:
#  4 4 -> 2 2
#  5 6 -> 2 3

s = int(input('введите сумму двух чисел: '))
p = int(input('введите произведение двух чисел: '))

x = 1
y = 1

sum = 0
multy = 0

# while (sum != s) and (multy != p):
for x in range(s):
    if (sum == s) and (multy == p): 
            break
    for y in range(p):
        sum = x + y
        multy = x * y
        if (sum == s) and (multy == p): 
            print(f' x = {x}, y = {y}')
            break

