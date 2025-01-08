from colorama import init, Fore, Back

# Initialize colorama
init()
number = input("enter a value: ")
if len(number) == 9:
    number = str(number)[1:]  # Удалить первую цифру ()
    formatted_number = "+7 ({}) {}-{}-{}".format(number[:3], number[3:6], number[6:9])
    print(formatted_number)
elif number.isdigit() :
   number = str(number)
elif len(number) == 9 and number.isdigit():
    print(Fore.RED + " " + "error len or letters(Object)(", number, ")is not defined try 9 characters or numbers ")

if len(number) == 9:
    number = str(number)[1:]  # Удалить первую цифру ()
    formatted_number = "+7 ({}) {}-{}-{}".format(number[:3], number[3:6], number[6:9])
    print(formatted_number)
elif len(number)!= 9 or len(number) < 9 or len(number)>9:

    print(Fore.RED+" "+"error len or letters(Object)(", number ,")is not defined try 9 characters or numbers ")
