n = int (input("enter n: "))
a = 1
b = 1
c = a + b
result = '1 1 2 '
while c <= n :
    a, b = b, c
    c = a + b
    result += f'{c} '
print(result)