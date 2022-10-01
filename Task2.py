a = [2, 3, 4, 5, 6]
b = [2, 3, 5, 6]

a[0] *= a[4]
a[1] *= a[3]
a[2] *= a[2]
if 5 in a:
    a.remove(5)
    if 6 in a:
        a.remove(6)
print(a)

b[0] *= b[3]
b[1] *= b[2]
if 5 in b:
    b.remove(5)
    if 6 in b:
        b.remove(6)
print(b)

