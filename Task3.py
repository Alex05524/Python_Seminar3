from random import uniform

def Get_Numbers (n, a, b):
    return [round(uniform(a,b), 2) for i in range(n)]

def Different(numbers):
    num = [round(x - int(x), 2) for x in numbers]
    return max(num) - min(num)

n = 5
A = 1
b = 10
numbers = Get_Numbers(n, A, b)

print (numbers)
print(Different(numbers))