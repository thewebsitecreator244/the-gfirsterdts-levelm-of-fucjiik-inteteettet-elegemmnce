A = float(input("enter a: "))
B = float(input("enter b: "))

quotient = 0
while A >= B:
    A -= B
    quotient += 1

remainder = A

print(quotient)
print(remainder)



