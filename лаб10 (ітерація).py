import timeit
import random
import numpy as np
def factorial(x):
    f = 1
    a = 0
    while a != x:#цмкл працює поки а не стане =0
        f *= x - a
        a += 1
    print(f)


def i(n):
    while n > 9:
        i = int(n % 10)
        n = n // 10
        n = n + i
    return n


def i_2(arr, max_num=0):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if max_num < arr[i][j]:
                max_num = arr[i][j]
    return max_num


while True:
    a=int(input("x:"))
    print(factorial(a))
    print(i(a))
    x = [random.randint(-5, 5) for i in range(10)]
    print(i_2(x))
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print(f"програма виконувалася {t} секунд")
    print(" ")
    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break
