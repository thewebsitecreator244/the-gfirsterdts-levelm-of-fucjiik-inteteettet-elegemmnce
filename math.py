import math
a = int(input("enter math : "))
s = 0
for i in range (1,a+1):
    s += math.factorial(i)

print(s)