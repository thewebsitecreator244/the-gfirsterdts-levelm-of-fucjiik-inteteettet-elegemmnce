a = int(input('enter a: '))
s = 0


for i in range(1, a+1):
    if i % 2 == 0:
     s -= i ** i
    elif i % 2 != 0:
        s += i ** i
print(s)
