a = int(input("enter a value: "))
b = int(input("enter b value: "))
c = int(input("enter c value: "))
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)