year2 = int(input("enter the year: "))
if year2 % 2 == 0 and year2 % 100 != 0 or year2 % 400 == 0:
    print(1)
else:
    print(0)