alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
stringToEncrypt = input("please enter a message to encrypt: " "")
stringToEncrypt = stringToEncrypt.upper()
shiftAmount = int(input("please enter a whole number from 1-25 to be your key: "
                         ""))
encryptedString = ""
for currentCharacter in stringToEncrypt:
    position = alphabet.find(currentCharacter)
    newPosition = position + shiftAmount
    if currentCharacter in alphabet:
        encryptedString = encryptedString + alphabet[newPosition]
    else:
        encryptedString = encryptedString + currentCharacter
print(" your encypted message is",encryptedString)
