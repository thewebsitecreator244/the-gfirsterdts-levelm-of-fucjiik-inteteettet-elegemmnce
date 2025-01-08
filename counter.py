a = input("enter digit (digit must be 3 numbers long): ")
counter = 0
if int(a[0]) % 2 == 0 and len(a) == 3:
    counter += 1
if int(a[1]) % 2 == 0 and len(a) == 3:
    counter += 1
if int(a[2]) % 2 == 0 and len(a) == 3:
    counter += 1
print(counter)