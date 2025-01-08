from colorama import Fore, Back, Style, init

init()




a = (input("enter a value: "))
if len(a) == 4:
   print( str(int(a[0])**2) + str(int(a[1])**2)+str(int(a[2])**2) +str(int(a[3])**2))
else:
   print(Fore.RED+"error len(object)(",a,")isn't defined try 4 characters")