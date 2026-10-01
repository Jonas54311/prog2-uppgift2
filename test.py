from random import choices

a = [1, 2, 3, 4, 5, 6]
b = choices(a, k=3)
b[0] = 9
print(a)
print(b)