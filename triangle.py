a = int(input("введите число a для первово угла треугольника: "))
b =int(input("введите число b: "))
c =int(input("введите число c: "))
if a + b > c and b + c > a and a + c > b:
    print("можно")
else:
    print("нельзя")
