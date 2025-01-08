years = int(input("enter years number: "))
money = int(input("enter money number:"))
YeArcOuNt = years - 2
yearspecial = 0
while YeArcOuNt > -2 :
    yearspecial = yearspecial + 1
    print(yearspecial,"year(s)",money,"money to pay")
    money = money * 2
    YeArcOuNt = YeArcOuNt - 1
    print()
print()



