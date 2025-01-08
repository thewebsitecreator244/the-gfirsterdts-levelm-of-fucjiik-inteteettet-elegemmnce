
a = int(input("enter math : "))
s = 0
for i in range (1,a+1):
    small = 1
    for j in range (1,i+1):
        small *= j
    if i % 2 == 0:
        s -= small
    else:
        s += small
print(s)