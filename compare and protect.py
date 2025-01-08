a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
if a == b and b == c:
    print(d)
elif b == c and c == d:
    print(a)
elif c == d and d == a:
    print(b)
else:
    print(c)