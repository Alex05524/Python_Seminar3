# Задайте число. 
# Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите число: '))

def fibo(k):
    numbers = []
    a, b = 1, 1
    for i in range(k-1):
        numbers.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (k):
        numbers.insert(0, a)
        a, b = b, a - b
    return numbers

numbers = fibo(k)
print(f"Для k = {numbers.index(0)} список будет выглядеть так: {fibo(k)}")
