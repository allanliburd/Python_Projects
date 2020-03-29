##
# Secret Message - encrypt a message using simple substitution method
##
alphabet = 'abcdefhijklmnopqrstuvwxyz'
numAndPunct = '0123456789!@#$%^&*()-+_=~` '
encryptedMsg = ''

message  = input("Please enter a message : ")
key = input("Please enter a key (1-26) : ")
key = int(key)

for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % len(alphabet)
        newChar = alphabet[newPosition]
        #print("the new character is : ", newChar)
        encryptedMsg += newChar
    elif character in numAndPunct:
        position = numAndPunct.find(character)
        newPosition = (position - key) % len(numAndPunct)
        newChar = numAndPunct[newPosition]
        encryptedMsg += newChar 

print("The encrypted message is : ", encryptedMsg)
