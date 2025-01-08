a = int(input('enter a: '))
s = 0


for i in range(1, a+1):
    if i % 3 == 0:
     s += i
print(s)