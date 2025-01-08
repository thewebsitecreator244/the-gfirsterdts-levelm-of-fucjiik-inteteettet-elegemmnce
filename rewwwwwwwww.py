n = int(input('enter N: '))
s = 1
for i in range(1, n+1):
    s /= i
print(s)