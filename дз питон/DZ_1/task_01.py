# Задача 1: Найдите сумму цифр трехзначного числа.
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

num = int(input('Введите трехзначное число: '))

if num < 1000 and num > 99:
    result1 = (num//10)//10   # 1
    result2 = (num//10) % 10  # 2
    result3 = num % 10  # 3
    
    res = result1 + result2 + result3

    print(res)

else:
    print('некорректный ввод')
