a = int(input("a=: "))
b = int(input("b=: "))
c = int(input("c=: "))
if a == b and b == c:
    print(3)
elif a == b or b == c or c == a:
    print(2)
else:
    print(0)