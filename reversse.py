n = int(input("enter N so we can reverse you number: "))
reversed_number = 0
while n > 0:
    digit = n % 10
    reversed_number = reversed_number * 10 + digit
    n = n // 10
if str (n) [0] == '0':
    reversed_number = '0' + str(reversed_number)
    print(reversed_number)
else:
    print(reversed_number)



