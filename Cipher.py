# User's Input 
import random

action = input ("Chose to [e]encrypt or [d]decrypt:")
password = input("Enter your password: ").lower()
key = int(input("Enter the key:"))


#Encrypting the character based on password and key 
def password_key ():
    new_password = []
    for i in password:
        
        numbers = "1","2","3","4","5","6","7","8","9"
        char1 ='a', 'b', 'c', 'd', 'e', 'f', 'g' 
        char2 = 'h', 'i', 'j', 'k', 'l', 'm', 'n'
        char3 = 'o', 'p', 'q', 'r', 's', 't' 
        char4 = 'u', 'v', 'w', 'x', 'y', 'z'
        characters = char1, char2, char3, char4, numbers

        if i  in numbers:
            i = 1**key
            new_password.extend([i])

        if i  in char1:
            i = 2**key
            new_password.extend([i])

        if i  in char2:
            i = 3**key
            new_password.extend([i])   

        if i  in char3:
            i = 4**key
            new_password.extend([i]) 

        if i  in char4:
            i = 5**key
            new_password.extend([i]) 

        if i != characters:
            i = 5**key
            new_password.extend([i])
    
    return(sum(new_password))


# random number generator  to create random characters in text
def inputing ():

###Checking the characters range
#for i in range(1,200):
    #print("{}<=>{}".format(i,chr(i)))

# Range of character is from 32 to 126:
    a = 1
    b = random.randrange(1,2)
    c = random.randrange(0,6)
    d = random.randrange(1,3)
    e = random.randrange(2,9)
    three_numbers = f"{a}{b}{c}"
    two_numbers = f"{d}{e}"
    choosing_from = three_numbers,two_numbers
    result = random.choice(choosing_from)

    return result

#Encrypting the message
if action == "e" or action == "encrypt":
    data = input("Write a measage to encrypt: ")
    text = ""
    for char in data:

# command to keep character within the range 
        char_ord = ord(char)
        if 32 <= char_ord <= 126:
            char_ord -= 32
            char_ord += password_key()
            char_ord = char_ord % 94
            char_ord += 32
            text += str(char_ord) + " " + str(inputing()) + " "

        else:
            text += str(char_ord) + " " + str(inputing()) + " "
    print("Cipher:")
    print("{}".format(text))

#Decrypting the message
elif action == "d" or action == "decrypt":
    data = input("Write an encrypted measage to decrypt: ")
    text = ""
    data = data.split()
    data = data[::2]
    
    for number in data:
        number= int(number)
        if 32 <= number <= 126:
            number-= 32
            number -= password_key()
            number = number % 94
            number += 32
            letter= chr(number)
            text += letter
        else:
            text += chr(number)
    print(text)


else:
    print("Error")

