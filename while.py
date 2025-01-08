a = int(input("enter first number: "))
b = int(input("enter last number: "))
range = input("normal range a<b  or reversed range b<a:  ")
if range == 'normal':
    while a < b:
        print(a)
        a = a + 1
    print(b)
elif range == 'reversed':
    while b < a :
        print(a)
        a = a - 1
    print(b)
else:
  print("we accept only 'normal' and 'reversed'")
  range = input("normal range a<b or reversed range b<a: ")
  if range == 'normal':
      while a < b:
          print(a)
          a = a + 1
          print(b)
  elif range == 'reversed':
      while b < a:
          print(a)
          a = a - 1
      print(b)
  else:
      print("we accept only 'normal' and 'reversed'")
