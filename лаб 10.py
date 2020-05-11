# Лічерп Артем
import timeit
import random
import numpy as np



def factorial(n):
    if type(n) is not int:  # якщо користувач вів не число йому напишить ошибку
        raise ValueError('factorial() only accepts integralvalues')

    if n < 0:  # якщо користувач вів число меньшь 0 напишить що факторіал не може бути відємним
        raise ValueError('factorial() not defined for negativevalues')

    if n == 0:  # якщо число =0 то вибє 1
        return 1
    else:  # якщо жодна из перед умов не спрацивали працює рекрсія
        return n * factorial(n - 1)


def f(x):
    if x == 1:
        return 0
    elif x == 2:
        return 1
    else:  # якщо жодна из перед умов не спрацивали працює рекрсія
        return f(x - 1) + f(x - 2)


def ind(x):
    n = 0
    k = -1

    n = x.pop()  #видаляємо сотінай елемер так додаємо в n
    k += 1
    if n == max(x):
        print('Максимальний елемент:', n, 'Його індекс:', k)
    else:
        ind(x)


while True:
    x = int(input("input: "))
    print(factorial(x))
    print(f(x))
    a = [random.randint(-5, 5) for i in range(10)]
    max1 = max(a)
    a.reverse()
    print(a)
    print(ind(a))
    t = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
    print(f"програма виконувалася {t} секунд")
    print(" ")
    if input('Нажмите "Enter" (введите пустую строку (\'\')) для перезапуска: ') == '':
        continue
    break
