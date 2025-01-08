def decalculate():
    quit()
a = int(input("enter a value: "))
b = int(input("enter b value: "))
c = input("enter a mathematical symbol: ")
if c not in ("+","-","*","/") or len(c) != 1:
    print("sorry the leght of c must be equal to 1 and the symbols to(+,-,*,/)")
    decalculate()
while 'true':
    if c == "+":
        print(a + b)
    elif c == "-":
        print(a - b)
    elif c == "*":
        print(a * b)
    elif c == "/":
        print(a / b)
    decalculate()