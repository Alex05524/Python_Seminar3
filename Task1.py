# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.

a = [2, 3, 5, 9, 3]
sum = 0
for i in range(1, len(a), 2):
    sum = sum + a[i]

print(f"на нечётных позициях элементы {i} и {a[i]}, ответ: {sum}")
    
