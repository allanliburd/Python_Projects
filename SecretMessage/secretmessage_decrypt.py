##
# Secret Message - decreypt a message using simple substitution method
##
from secretmessage import encryptedMsg, alphabet, numAndPunct, key

decryptedMsg = ''

for character in encryptedMsg:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position - key) % len(alphabet)
        newChar = alphabet[newPosition]
        #print("the new character is : ", newChar)
        decryptedMsg += newChar
    elif character in numAndPunct:
        position = numAndPunct.find(character)
        newPosition = (position + key) % len(numAndPunct)
        newChar = numAndPunct[newPosition]
        decryptedMsg += newChar 

print("The decrypted message is : ", decryptedMsg)