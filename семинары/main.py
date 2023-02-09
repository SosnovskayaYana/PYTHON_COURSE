def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)

list1 = []

for i in range(1, 10):
    list1.append(fib(i))
print(list1)